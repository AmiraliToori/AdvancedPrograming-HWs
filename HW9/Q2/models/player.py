
import pygame as pg

# Player Icon 
PLAYER_ICON_PATH = "material/icons8-human-50.png"
PLAYER_IMG = pg.image.load(PLAYER_ICON_PATH)


class Player:
    PLAYER_X = 375
    PLAYER_Y = 550
    
    
    def __init__(self, screen) -> None:
        self.screen = screen
        self.x = Player.PLAYER_X
        self.y = Player.PLAYER_Y
        
        self.lives = 3
        self.is_lose = False
        self.score = 0
        
        
    def draw(self) -> None:
        self.screen.blit(PLAYER_IMG, (self.x, self.y))
    
    def earn_score(self) -> None:
        self.score += 5
        
    def decrease_score(self) -> None:
        self.score -= 3
    
    def decrease_lives(self) -> None:
        self.lives -= 1
        
    def reset_lives(self) -> None:
        self.lives = 3