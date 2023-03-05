import pygame as pg
import math
#from game import player
import player as p
import random

clock = pg.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200 #probs should change
SCREEN_HEIGHT = 900 #probs should change
FLOOR = 440

def vertical_collision(player): 
    player.update_gravity()
    if player.rect.bottom > FLOOR and not player.swimming: 
        player.rect.bottom = FLOOR
        player.direction.y = 0
        player.on_floor = True
    if player.rect.bottom < FLOOR and player.swimming:
        player.swimming = False
        player.gravity = 0.8
        player.rect.bottom = FLOOR
        player.direction.y = 0
        player.on_floor = True
    if player.on_floor and player.direction.y < 0 or player.direction.y > 1: 
            player.on_floor = False




def main():
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg = pg.image.load("assets/scrollbackground.png").convert()
    bg_width = bg.get_width()

    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

    frog = p.Player((150, 450))
    player = pg.sprite.GroupSingle()
    player.add(frog)

    # always two obstacles being constantly updated 
    obstacle = pg.image.load("assets/reeds.png").convert_alpha()
    obstacle = pg.transform.rotozoom(obstacle, 0, 0.5)
    obstacle_x = 700
    obstacle_speed = 5
    obstacle2 = pg.image.load("assets/reeds.png").convert_alpha()
    obstacle2 = pg.transform.rotozoom(obstacle2, 0, 0.5)
    obstacle2_x = 1100


    run = True
    while run:
        clock.tick(FPS)

        for i in range(0, tiles):

            screen.blit(bg, (i * bg_width + scroll, 0))

        scroll -= 5
        vertical_collision(frog)
        player.update()
        player.draw(screen)
        

        if abs(scroll) > bg_width:
            scroll = 0

        # obstacle updating 
        if(abs(obstacle_x - obstacle2_x) < 200):
            obstacle2_x += 150
        o_rect = screen.blit(obstacle, (obstacle_x, 360))
        obstacle_x -= obstacle_speed
        obstacle_rand = random.randint(1200, 1300)
        if obstacle_x < -300:
            obstacle_x = obstacle_rand
        o2_rect = screen.blit(obstacle2, (obstacle2_x, 360))
        
        obstacle2_x -= obstacle_speed
        if obstacle2_x < -300:
            obstacle2_x = obstacle_rand + 100

        # collision detection
        frog_rect = frog.rect
        
        if o_rect.colliderect(frog_rect) or o2_rect.colliderect(frog_rect):
            print("collided")
            #return

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main()