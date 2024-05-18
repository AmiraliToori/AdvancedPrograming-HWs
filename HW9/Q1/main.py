

import pygame as pg
from random import choice, randint
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
VALUE = 0.2

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


# Objects
CIRCLE_PATH = "material/icons8-circle-30.png"
CIRCLE_IMG = pg.image.load(CIRCLE_PATH)

SQUARE_PATH = "material/icons8-square-30.png"
SQUARE_IMG = pg.image.load(SQUARE_PATH)

TRIANGLE_PATH = "material/icons8-triangle-30.png"
TRIANGLE_IMG = pg.image.load(TRIANGLE_PATH)

# Score
score = 0


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
    text = font.render(f"{score}", True, "black", COLOR_BACKGROUND)
    text_box = text.get_rect()
    text_box = (750, 5)
    screen.blit(text, text_box)



def draw_objects() -> tuple:
    lst = [SQUARE_IMG, CIRCLE_IMG, TRIANGLE_IMG]
    
    x = randint(-10, 750)
    y = randint(30, 550)
    screen.blit(choice(lst), (x, y))
    
    return x, y

def is_collision(object_x: int,
                 object_y: int,
                 player_x: int,
                 player_y: int) -> bool:
    
    distance = math.sqrt(math.pow(object_x - player_x, 2) + math.pow(object_y - player_y, 2))

    if distance < 10:
        return True
    else:
        return False
    
    
def main() -> None:
    player_x = 760
    player_y = 550
    
    pg.init()    
    
    running = True
    while running:
        
        screen.fill(COLOR_BACKGROUND)
        screen.blit(TIMER_IMG, TIMER_X_Y)
        pg.draw.line(screen, COLOR_LINE, START_LINE, END_LINE, WIDTH_LINE)
        
        time = pg.time.get_ticks() // 1000
        timer_text(time)
        
        
        object_x, object_y = draw_objects()
        
        is_collision(object_x, object_y, player_x, player_y)
            
            
        score_text(score)
        
        keys = pg.key.get_pressed() 
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
        if keys[pg.K_RIGHT]:
            player_x += VALUE
        if keys[pg.K_LEFT]:
            player_x -= VALUE
        if keys[pg.K_UP]:
            player_y -= VALUE
        if keys[pg.K_DOWN]:
            player_y += VALUE
        
        
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