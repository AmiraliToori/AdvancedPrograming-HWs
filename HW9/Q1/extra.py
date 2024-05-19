

import pygame as pg
from random import randint, choice
from icecream import ic


# Objects
CIRCLE_PATH = "material/icons8-circle-30.png"
CIRCLE_IMG = pg.image.load(CIRCLE_PATH)

SQUARE_PATH = "material/icons8-square-30.png"
SQUARE_IMG = pg.image.load(SQUARE_PATH)

TRIANGLE_PATH = "material/icons8-triangle-30.png"
TRIANGLE_IMG = pg.image.load(TRIANGLE_PATH)

SHAPE_LIST = {"square": SQUARE_IMG, "circle": CIRCLE_IMG, "triangle": TRIANGLE_IMG}

def generate_target() -> str:
    target, temp = choice(list(SHAPE_LIST.items()))
    return target


class Shape:
    
    def __init__(self) -> None:
        
        self.x = randint(-10, 750)
        self.y = randint(30, 550)
        self.is_exists = True
        self.name, self.shape = choice(list(SHAPE_LIST.items()))
        
        
    def draw(self,
             screen) -> None:
        if self.is_exists:
            screen.blit(self.shape,(self.x, self.y))
    
    def death(self) -> None:
        self.is_exists = False

    def coordinates(self) -> tuple:
        return self.x, self.y
    

class Timer:
    
    
    def __init__(self) -> None:
        self.time = pg.time.get_ticks() // 1000
    
    def end(self) -> float:
        JUST_ONCE = True
        if JUST_ONCE:
            time = self.time
            JUST_ONCE = False
            return time


time = Timer()

print(time.end())