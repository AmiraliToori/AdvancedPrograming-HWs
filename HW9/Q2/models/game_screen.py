
import pygame as pg


from .objects import DrawIcon, DrawLine, DrawText
from .player import Player



# Score
SCORE_FONT_SIZE = 20
SCORE_FONT_COLOR = "black"
SCORE_FONT_COLOR_BACKGROUND = "white"
SCORE_FONT_X = 690
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
VELOCITY_FONT_X = 680
VELOCITY_FONT_Y = 580


# Timer Icon
TIMER_ICON_PATH = "material/icons8-timer-30.png"
TIMER_IMG = pg.image.load(TIMER_ICON_PATH)
TIMER_ICON_X = 0
TIMER_ICON_Y = 0

# Timer Font
TIMER_FONT_SIZE = 20
TIMER_FONT_COLOR = "black"
TIMER_FONT_COLOR_BACKGROUND = "white"
TIMER_FONT_X_POS = 35
TIMER_FONT_Y_POS = 0

# color line
LINE_COLOR = 'black'
START_LINE__POSITION = (0, 30)
END_LINE_POSITION = (800, 30)

class GameScreen:
    
    
    def __init__(self, screen, velocity_value, time, gamer) -> None:
        
        
        self.score = DrawText(f"SCORE: {gamer.score}",
                                SCORE_FONT_SIZE,
                                SCORE_FONT_COLOR,
                                SCORE_FONT_COLOR_BACKGROUND,
                                screen,
                                SCORE_FONT_X,
                                SCORE_FONT_Y)
        
        self.lives = DrawText(f"LIVES: {gamer.lives}",
                    LIVES_FONT_SIZE,
                    LIVES_FONT_COLOR,
                    LIVES_FONT_COLOR_BACKGROUND,
                    screen,
                    LIVES_FONT_X,
                    LIVES_FONT_Y)
        
        self.line_separator = DrawLine(screen,
                                        LINE_COLOR,
                                        START_LINE__POSITION,
                                        END_LINE_POSITION)
        
        self.timer_icon = DrawIcon(screen,
                                    TIMER_IMG,
                                    TIMER_ICON_X,
                                    TIMER_ICON_Y)
        
        
        self.timer_text = DrawText(f"{time}",
                                    TIMER_FONT_SIZE,
                                    TIMER_FONT_COLOR,
                                    TIMER_FONT_COLOR_BACKGROUND,
                                    screen,
                                    TIMER_FONT_X_POS,
                                    TIMER_FONT_Y_POS)
        
        self.velocity = DrawText(f"VELOCITY: {velocity_value}",
                                    VELOCITY_FONT_SIZE,
                                    VELOCITY_FONT_COLOR,
                                    VELOCITY_FONT_COLOR_BACKGROUND,
                                    screen,
                                    VELOCITY_FONT_X,
                                    VELOCITY_FONT_Y)
        
    def draw(self) -> None:
            
        self.score.draw()
        self.lives.draw()
        
        self.line_separator.draw()
        
        self.timer_icon.draw()
        self.timer_text.draw()
        self.velocity.draw()