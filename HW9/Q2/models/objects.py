
import pygame as pg


# Font
FONT_PATH = "material/Material_Sans.ttf"

# Anti alias option
ANTI_ALIAS_OPTION = True


class DrawText:
    
    def __init__(self,
                text_input: str,
                font_size: int,
                text_color: tuple | str,
                background_color: tuple | str,
                screen,
                x_pos: int,
                y_pos: int) -> None:
        
        self.text_input = text_input
        self.font_size = font_size
        self.text_color = text_color
        self.background_color = background_color
        self.screen = screen
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def draw(self) -> None:
        font = pg.font.Font(FONT_PATH, self.font_size)
        text = font.render(self.text_input, ANTI_ALIAS_OPTION, self.text_color, self.background_color)
        self.screen.blit(text, (self.x_pos, self.y_pos))



class DrawLine:
    
    
    def __init__(self,
                 screen,
                 color: str,
                 start_line_pos,
                 end_line_pos):
        self.screen = screen
        self.color = color
        self.start_line_pos = start_line_pos
        self.end_line_pos = end_line_pos
    
    def draw(self):
        pg.draw.line(self.screen,
                     self.color,
                     self.start_line_pos,
                     self.end_line_pos)
        
        
class DrawIcon:
    
    
    def __init__(self, screen, source, x_pos, y_pos) -> None:
        self.screen = screen
        self.source = source
        self.x_pos = x_pos
        self.y_pos = y_pos
        
    def draw(self) -> None:
        self.screen.blit(self.source,
                         (self.x_pos,
                         self.y_pos))
        



    
    
