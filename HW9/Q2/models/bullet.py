

import pygame as pg
from .player import Player
from icecream import ic
import math

# Ball Icon
BALL_ICON_PATH = "material/icons8-ball-30.png"
BALL_IMG = pg.image.load(BALL_ICON_PATH)


class Bullet:
    
    def __init__(self, screen, velocity) -> None:
        
        self.screen = screen
        
        self.pos = (Player.PLAYER_X, Player.PLAYER_Y + 30)
        
        x , y = Player.PLAYER_X, Player.PLAYER_Y
        mx, my = pg.mouse.get_pos()
        
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0]/length, self.dir[1]/length)
            
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = BALL_IMG
        self.bullet = pg.transform.rotate(self.bullet, angle)
        
        self.velocity_x = velocity * math.cos(angle)
        self.velocity_y = velocity * math.sin(angle)
        
        self.gravity = 9.8
        self.velocity = velocity
        self.rect = self.bullet.get_rect(center = self.pos)
    
    def update(self, time_throw):
        
        
        # dist_x = (self.velocity_y * time_throw * -0.5 * self.gravity * (time_throw)**2)
        # dist_y =  self.velocity_x * time_throw
        # new_x = round(dist_x + Player.PLAYER_X)
        # new_y = round(Player.PLAYER_Y - dist_y)
        # self.pos = (new_x, new_y)
        
        self.pos = (self.pos[0]+self.dir[0]*self.velocity, 
                    self.pos[1]+self.dir[1]*self.velocity)

    def draw(self, screen):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        ic(self.rect)
        screen.blit(self.bullet, bullet_rect)
        