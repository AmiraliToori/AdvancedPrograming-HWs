
import pygame as pg
from extra import Shape, generate_target
import math

# Display Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR_BACKGROUND = (240, 219, 60)

# Display and Caption
pg.display.set_caption("Question -1-")
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Player
PLAYER_ICON_PATH = "material/icons8-human-50.png"
PLAYER_IMG = pg.image.load(PLAYER_ICON_PATH)
SPEED = 0.2

# Timer Icon
TIMER_ICON_PATH = "material/icons8-timer-30.png"
TIMER_IMG = pg.image.load(TIMER_ICON_PATH)
TIMER_X_Y = (0, 0)

# Timer
TIMER_TEXT_X_Y = (0, 60)

# LINE
COLOR_LINE = "black"
START_LINE = (0, 30)
END_LINE = (800, 30)
WIDTH_LINE = 2

# Font
FONT_PATH = "material/Material_Sans.ttf"
FONT_SIZE = 20
GAME_OVER_FONT_SIZE = 50
MESSAGE_FONT_SIZE = 50

# Score
score = 0

# Target
TARGET = generate_target()

# Music 
EARN_SCORE_SOUND_PATH = "material/pickupCoin.wav"
LOSE_SCORE_SOUND_PATH = "material/hitHurt.wav"

# Number of Objects
NUMBER_OF_OBJECTS = 15

def player(x: int,
           y: int) -> None:
    screen.blit(PLAYER_IMG, (x, y))
    
    
def timer_text(time: int) -> str:
    font = pg.font.Font(FONT_PATH, FONT_SIZE)
    text = font.render(f"{time}", True, "black", COLOR_BACKGROUND)
    text_box = text.get_rect()
    text_box = (40, 5)
    screen.blit(text, text_box)

def score_text(score: int) -> None:
    font = pg.font.Font(FONT_PATH, FONT_SIZE)
    text = font.render(f"SCORE: {score}", True, "black", COLOR_BACKGROUND)
    text_box = text.get_rect()
    text_box = (710, 5)
    screen.blit(text, text_box)

shape_lst = []
[shape_lst.append(Shape()) for _ in range(NUMBER_OF_OBJECTS)]



def draw_objects(shape) -> tuple:
    shape.draw(screen)
    x , y = shape.coordinates()
    return x, y

def is_collision(shape: Shape,
                player_x: int,
                player_y: int) -> bool:
    global score
    
    if shape:
        object_x, object_y = shape.coordinates()
    
        distance = math.sqrt(math.pow(object_x - player_x, 2) + math.pow(object_y - player_y, 2))
        if shape.is_exists:
            if distance < 20:
                if shape.name == TARGET:
                    score += 5
                    play_music(True)
                else: 
                    score -= 2
                    play_music(False)
                    
                shape.death()
                shape_lst.remove(shape)
                del shape
                
            else:
                return False
    else:
        return 

def play_music(entry: bool) -> None:
    
    EARN_SCORE_SOUND = pg.mixer.Sound(EARN_SCORE_SOUND_PATH)
    LOSE_SCORE_SOUND = pg.mixer.Sound(LOSE_SCORE_SOUND_PATH)
    
    if entry:
        pg.mixer.Sound.play(EARN_SCORE_SOUND)
    else:
        pg.mixer.Sound.play(LOSE_SCORE_SOUND)
        


def game_over_text(time: int) -> None:
    
    GAME_OVER_TEXT = f'''GAME OVER SCORE: {score}, TIME: {time}'''
    screen.fill(COLOR_BACKGROUND)
    font = pg.font.Font(FONT_PATH, GAME_OVER_FONT_SIZE)
    text = font.render(GAME_OVER_TEXT, True, COLOR_BACKGROUND, "black")
    text_box = text.get_rect()
    text_box.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen.blit(text, text_box) 
    pg.time.wait(1000)
    


def is_game_end(shape_lst: list,
                TARGET: str) -> int:
    lst = []
    
    for shape in shape_lst:
        
        if shape.name != TARGET:
            lst.append(False)
        else:
            lst.append(True)
            
    if not any(lst):
        return 2
    else:
        return 1
    
        
def message_text() -> None:
    screen.fill(COLOR_BACKGROUND)
    font = pg.font.Font(FONT_PATH, MESSAGE_FONT_SIZE)
    text = font.render(f"The TARGET is {TARGET}", True, "black", COLOR_BACKGROUND)
    text_box = text.get_rect()
    text_box.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen.blit(text, text_box)

def main() -> None:
    
    player_x = 760
    player_y = 550
    
    global score
    
    pg.init()    
    pg.mixer.init()
    
    num = 0
    running = True
    
    while running:
        
        match num:
            
            case 1:
                screen.fill(COLOR_BACKGROUND)
                screen.blit(TIMER_IMG, TIMER_X_Y)
                pg.draw.line(screen, COLOR_LINE, START_LINE, END_LINE, WIDTH_LINE)
                
                # if screen_option != 2:
                time = pg.time.get_ticks() // 1000
                
                timer_text(time)
                
                for shape in shape_lst:
                    draw_objects(shape)
                    
                    if shape:
                        is_collision(shape, player_x, player_y)
                
                num = is_game_end(shape_lst, TARGET)
                
                score_text(score)
                
            case 2: 
                game_over_text(time)
                
            case 0:
                message_text()
            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_RIGHT]:
            player_x += SPEED
        if keys[pg.K_LEFT]:
            player_x -= SPEED
        if keys[pg.K_UP]:
            player_y -= SPEED
        if keys[pg.K_DOWN]:
            player_y += SPEED
        if keys[pg.K_q]:
            running = False
        if keys[pg.K_SPACE]:
            num = 1
            
        
        
        if player_x <= -10:
            player_x = -10
        elif player_x >= 760 :
            player_x = 760
            
        if player_y <= 30:
            player_y = 30
        elif player_y >= 550:
            player_y = 550
        
        player(player_x, player_y)
        pg.display.flip()
            
    
if __name__ == "__main__":
    main()
    pg.quit()