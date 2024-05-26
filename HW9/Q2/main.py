
import pygame as pg
from models import game_screen, bullet, target, player
import math
from icecream import ic

# Display option
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLOR_BACKGROUND = 'white'




def main():
    run = True
    screen_num = 1
    velocity_value = 2
    
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    clock = pg.time.Clock()
    
    target_ball = target.Target(screen)
    bullet_ball = bullet.Bullet(screen, velocity_value)
    gamer = player.Player(screen)
    balls = []
    
    

    while run:
        clock.tick(60)
        match screen_num:
            
            case 1:
                
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
                balls.remove(ball)
            
        
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
            
    
