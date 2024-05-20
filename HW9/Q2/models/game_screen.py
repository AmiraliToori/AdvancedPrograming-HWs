
import pygame as pg


# Font
FONT_PATH = "material/Material_Sans.ttf"

# Anti alias option
ANTI_ALIAS_OPTION = True

# Timer Font
TIMER_FONT_SIZE = 20
TIMER_FONT_COLOR = "black"
TIMER_FONT_COLOR_BACKGROUND = "white"
TIMER_FONT_X_POS = 35
TIMER_FONT_Y_POS = 5

# Timer Icon
TIMER_ICON_PATH = "material/icons8-timer-30.png"
TIMER_IMG = pg.image.load(TIMER_ICON_PATH)
TIMER_ICON_X = 0
TIMER_ICON_Y = 0

# color line
LINE_COLOR = 'black'

START_LINE__POSITION = (0, 30)
END_LINE_POSITION = (800, 30)




def draw_text(text: str,
              font_size: int,
              text_color: tuple | str,
              background_color: tuple | str,
              screen,
              x_pos: int,
              y_pos: int) -> None:
    
    font = pg.font.Font(FONT_PATH, font_size)
    text = font.render(text, ANTI_ALIAS_OPTION, text_color, background_color)
    screen.blit(text, (x_pos, y_pos))

def draw_timer(screen):
    time = pg.time.get_ticks() // 1000
    draw_text(f"{time}",
              TIMER_FONT_SIZE,
              TIMER_FONT_COLOR,
              TIMER_FONT_COLOR_BACKGROUND,
              screen,
              TIMER_FONT_X_POS,
              TIMER_FONT_Y_POS
              )
    screen.blit(TIMER_IMG, (TIMER_ICON_X, TIMER_ICON_Y))


def draw_line(screen):
    pg.draw.line(screen,
                 LINE_COLOR,
                 START_LINE__POSITION,
                 END_LINE_POSITION)


    
    
