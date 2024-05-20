


import pygame as pg
from random import randint

# Player Icon 
PLAYER_ICON_PATH = "material/icons8-human-50.png"
PLAYER_IMG = pg.image.load(PLAYER_ICON_PATH)

# Player position coordinates
PLAYER_X = 375
PLAYER_Y = 550

# Target Icon
TARGET_ICON_PATH = "material/icons8-circle-50.png"
TARGET_IMG = pg.image.load(TARGET_ICON_PATH)

# Ball Icon
BALL_ICON_PATH = "material/icons8-ball-30.png"
BALL_IMG = pg.image.load(BALL_ICON_PATH)


class Ball:
    
    def __init__(self, mass) -> None:
        self.x = PLAYER_X 
        self.y = PLAYER_Y
        self.mass = mass
    
    def throw(self, screen, velocity) -> None:
        if self.y >= 30:
            self.y -= velocity
            
            if self.y == 30:
                pass
        else:
            self.y 
        screen.blit(BALL_IMG, (self.x, self.y))    
            
    
    
    

ball = Ball()


class Player:
    
    def __init__(self) -> None:
        self.x = PLAYER_X
        self.y = PLAYER_Y
        self.lives = 3
        self.is_lose = False
        self.score = 0
        
    def throw(self, screen, velocity) -> None:
        ball.throw(screen, velocity)
    
    def draw(self, screen) -> None:
        screen.blit(PLAYER_IMG, (self.x, self.y))



class Target:
    
    def __init__(self) -> None:
        self.x = randint(0, 750)
        self.y = randint(40, 300)
        self.is_dead = True
        
    def draw(self, screen) -> None:
        screen.blit(TARGET_IMG, (self.x, self.y))
        
    def collision(self):
        self.is_dead = False








    


