
import pygame as pg
from random import randint

# Target Icon
TARGET_ICON_PATH = "material/icons8-circle-50.png"
TARGET_IMG = pg.image.load(TARGET_ICON_PATH)

class Target:
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.x = randint(300, 760)
        self.y = randint(200, 500)
        self.is_alive = True
        self.target = TARGET_IMG
        self.rect = TARGET_IMG.get_rect(center = (self.x, self.y))
        
    def draw(self) -> None:
        self.screen.blit(self.target, self.rect)
        
    def destroy(self):
        self.is_alive = False