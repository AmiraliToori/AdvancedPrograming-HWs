
import pygame as pg
from models import game_screen, bullet, target, player
from models.objects import DrawText
from icecream import ic
# Display option
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOR_BACKGROUND = 'white'

GAME_OVER_FONT_SIZE = 50
GAME_OVER_FONT_COLOR = 'black'
GAME_OVER_FONT_BACKGROUND_COLOR = 'white'
GAME_OVER_X = 50
GAME_OVER_Y = 250





def main():
    run = True
    screen_num = 1
    velocity_value = 2
    
    pg.init()
    pg.mixer.init()
    
    # Sounds Effect 
    EARN_SCORE_PATH = "material/pickupCoin.wav"
    EARN_SCORE_SOUND = pg.mixer.Sound(EARN_SCORE_PATH)

    LOST_SCORE_PATH = "material/hitHurt.wav"
    LOST_SCORE_SOUND = pg.mixer.Sound(LOST_SCORE_PATH)
    
    VICTORY_PATH = "material/VictorySound.mp3"
    VICTORY_SOUND = pg.mixer.Sound(VICTORY_PATH)
    
    GAME_OVER_PATH = "material/GameOverSound.mp3"
    GAME_OVER_SOUND = pg.mixer.Sound(GAME_OVER_PATH)
    
    BACKGROUND_MUSIC_PATH = "material/background_music.mp3"
    pg.mixer.music.load(BACKGROUND_MUSIC_PATH)
    
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pg.time.Clock()
    
    target_ball = target.Target(screen)
    
    gamer = player.Player(screen)
    
    game_over_text = DrawText(f"GAME-OVER, SCORE:{gamer.score}",
                              GAME_OVER_FONT_SIZE,
                              GAME_OVER_FONT_COLOR,
                              GAME_OVER_FONT_BACKGROUND_COLOR,
                              screen,
                              GAME_OVER_X,
                              GAME_OVER_Y)
    
    victory_text = DrawText(f"VICTORY, SCORE:{gamer.score}",
                              GAME_OVER_FONT_SIZE,
                              GAME_OVER_FONT_COLOR,
                              GAME_OVER_FONT_BACKGROUND_COLOR,
                              screen,
                              GAME_OVER_X,
                              GAME_OVER_Y)
    
    balls = []
    victory_list = []
    
    pg.mixer.music.play()
    while run:
        clock.tick(60)
        match screen_num:
            
            case 1:
                
                if not pg.mixer.music.get_busy():
                    pg.mixer.music.play()
                    
                screen.fill(COLOR_BACKGROUND)
                
                time = pg.time.get_ticks() // 1000
                main_screen = game_screen.GameScreen(screen, velocity_value, time, gamer)
                main_screen.draw()
                gamer.draw()
                target_ball.draw()
                
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        run = False
                    elif event.type == pg.KEYDOWN:
                    
                        if event.key == pg.K_v:
                            velocity_value += 0.1
                        elif event.key == pg.K_c:
                            velocity_value -= 0.1
                        elif event.key == pg.K_q:
                            run = False
        

                if pg.mouse.get_pressed()[0] == True and len(balls) == 0:
                    balls.append(bullet.Bullet(screen, velocity_value))
                
                for ball in balls:
                    time_throw = pg.time.get_ticks()
                    ball.draw(screen)
                    ball.update(time_throw)
                    
                    if not screen.get_rect().collidepoint(ball.pos):
                        
                        LOST_SCORE_SOUND.play()
                        
                        balls.remove(ball)
                        
                        gamer.decrease_score()
                        
                        gamer.decrease_lives()
                        
                        victory_list.clear()
                
                
                    if target_ball.rect.collidepoint(ball.pos):
                        
                        EARN_SCORE_SOUND.play()
                        
                        balls.remove(ball)
                        
                        gamer.earn_score()
                        
                        gamer.reset_lives()
                        
                        victory_list.append(True)
                        
                        target_ball = target.Target(screen)
                        
                        target_ball.draw()
                    
                    
                    
                    if gamer.lives == 0:
                        pg.mixer.music.stop()
                        GAME_OVER_SOUND.play()
                        screen_num = 2
                        
                        
                    
                    if len(victory_list) >= 10:
                        pg.mixer.music.stop()
                        VICTORY_SOUND.play()
                        screen_num = 3
                        
                        
                        
            
            case 2:
                
                screen.fill(COLOR_BACKGROUND)
                game_over_text = DrawText(f"GAME-OVER, SCORE:{gamer.score}, TIME:{time}",
                              GAME_OVER_FONT_SIZE,
                              GAME_OVER_FONT_COLOR,
                              GAME_OVER_FONT_BACKGROUND_COLOR,
                              screen,
                              GAME_OVER_X,
                              GAME_OVER_Y)
                
                game_over_text.draw()
                
                for event in pg.event.get():
                            if event.type == pg.QUIT:
                                run = False
                            elif event.type == pg.KEYDOWN:
                    
                                if event.key == pg.K_q:
                                    run = False
                
                
            case 3:
                
                screen.fill(COLOR_BACKGROUND)
                victory_text = DrawText(f"VICTORY, SCORE:{gamer.score}, TIME:{time}",
                              GAME_OVER_FONT_SIZE,
                              GAME_OVER_FONT_COLOR,
                              GAME_OVER_FONT_BACKGROUND_COLOR,
                              screen,
                              GAME_OVER_X,
                              GAME_OVER_Y)
                
                victory_text.draw()
                
                for event in pg.event.get():
                            if event.type == pg.QUIT:
                                run = False
                            elif event.type == pg.KEYDOWN:
                                if event.key == pg.K_q:
                                    run = False
                                    
        
        pg.display.flip()
        
        
if __name__ == "__main__":
    main()
    pg.quit()
    
    
    
    
    


            # dest_x, dest_y = pg.mouse.get_pos()

            # hypothesis = math.sqrt((dest_x - gamer.x)**2 + (dest_y - gamer.y)**2)
            # opposite_edge = math.sqrt(0 + (dest_y - gamer.y)**2)

            # angle_degree = math.degrees(math.acos(opposite_edge / hypothesis))

            # print(angle_degree)

            # # u = velocity
            # alpha = np.radians(angle_degree)
            # max_range = velocity**2 * np.sin(2*alpha)/gravity
            # max_height = velocity**2 * (np.sin(alpha))**2 / (2*gravity)
            # x_array = np.linspace(0, max_range, 20)
            # y_array = x_array * np.tan(alpha) - (1/2)* (gravity*x_array**2)/(velocity**2*(np.cos(alpha))**2)

            # print(x_array)
            # print(y_array)
            
    
