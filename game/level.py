import pygame as pg
import math
import random
from obstacles import *

clock = pg.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200 #probs should change
SCREEN_HEIGHT = 900 #probs should change

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pg.image.load("assets/scrollbackground.png").convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

# random load image
'''
obstacle = pg.image.load("assets/froggy.png")
obstacle_x = 700
obstacle_speed = 5
obstacle2 = pg.image.load("assets/froggy.png")
obstacle2_x = 1100
'''

obs = pg.sprite.Group()
obstacle_x = 700
obstacle2_x = 1100
ob = Obstacle(obstacle_x, obstacle2_x,(obstacle_x, 370))
ob2 = Obstacle(obstacle_x, obstacle2_x,(obstacle2_x, 370))
obs.add(ob)
obs.add(ob2)
obstacle_speed = 5

run = True
while run:
    clock.tick(FPS)

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    obs.draw(screen)
    obs.update(obstacle_speed)
    '''
    if(abs(obstacle_x - obstacle2_x) < 200):
        obstacle2_x += 150
    screen.blit(obstacle, (obstacle_x, 370))
    obstacle_x -= obstacle_speed
    obstacle_rand = random.randint(1200, 1300)
    if obstacle_x < -300:
        obstacle_x = obstacle_rand
    screen.blit(obstacle2, (obstacle2_x, 370))
    obstacle2_x -= obstacle_speed
    if obstacle2_x < -300:
        obstacle2_x = obstacle_rand + 100
    '''
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
pg.quit()