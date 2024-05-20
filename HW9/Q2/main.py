
import pygame as pg
from models import objects
from models import game_screen

# Display option
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOR_BACKGROUND = 'white'

# Player
PLAYER = objects.Player()

# Target
TARGET = objects.Target()

# Score
SCORE_FONT_SIZE = 20
SCORE_FONT_COLOR = "black"
SCORE_FONT_COLOR_BACKGROUND = "white"
SCORE_FONT_X = 700
SCORE_FONT_Y = 5

# Lives
LIVES_FONT_SIZE = 30
LIVES_FONT_COLOR = "black"
LIVES_FONT_COLOR_BACKGROUND = "white"
LIVES_FONT_X = 0
LIVES_FONT_Y = 570

# Velocity

VELOCITY_FONT_SIZE = 20
VELOCITY_FONT_COLOR = "black"
VELOCITY_FONT_COLOR_BACKGROUND = "white"
VELOCITY_FONT_X = 670
VELOCITY_FONT_Y = 580

def main():

    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    
    run = True
    screen_num = 1
    throw = True
    velocity = 0.5
    
    while run:
        match screen_num:
            case 1:
                screen.fill(COLOR_BACKGROUND)
                PLAYER.draw(screen)
                TARGET.draw(screen)
                game_screen.draw_timer(screen)
                game_screen.draw_line(screen)
                
                game_screen.draw_text(f"SCORE: {PLAYER.score}",
                                      SCORE_FONT_SIZE,
                                      SCORE_FONT_COLOR,
                                      SCORE_FONT_COLOR_BACKGROUND,
                                      screen,
                                      SCORE_FONT_X,
                                      SCORE_FONT_Y)
                
                game_screen.draw_text(f"LIVES: {PLAYER.lives}",
                                      LIVES_FONT_SIZE,
                                      LIVES_FONT_COLOR,
                                      LIVES_FONT_COLOR_BACKGROUND,
                                      screen,
                                      LIVES_FONT_X,
                                      LIVES_FONT_Y)
                
                game_screen.draw_text(f"VELOCITY: {velocity}",
                                      VELOCITY_FONT_SIZE,
                                      VELOCITY_FONT_COLOR,
                                      VELOCITY_FONT_COLOR_BACKGROUND,
                                      screen,
                                      VELOCITY_FONT_X,
                                      VELOCITY_FONT_Y)
                
                if not throw == True:
                    PLAYER.throw(screen, velocity)
                    
                
                
                    

        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_SPACE]:
            throw = False
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_v:
                    velocity += 0.1
                elif event.key == pg.K_c:
                    velocity -= 0.1
                elif event.key == pg.K_q:
                    run = False

        pg.display.flip()

if __name__ == "__main__":
    main()
    pg.quit()