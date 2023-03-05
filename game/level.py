import pygame as pg
import math
import random

clock = pg.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200 #probs should change
SCREEN_HEIGHT = 900 #probs should change

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pg.image.load("assets/scrollbackground.png").convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

obstacle = pg.image.load("assets/reeds.png")
obstacle = pg.transform.rotozoom(obstacle, 0, 0.5)
obstacle_x = 700
obstacle_speed = 5
obstacle2 = pg.image.load("assets/reeds.png")
obstacle2 = pg.transform.rotozoom(obstacle2, 0, 0.5)
obstacle2_x = 700

run = True
while run:
    clock.tick(FPS)

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    screen.blit(obstacle, (obstacle_x, 250))
    obstacle_x -= obstacle_speed
    if obstacle_x < -300:
        obstacle_x = random.randint(1300, 1400)
    screen.blit(obstacle2, (obstacle2_x, 250))
    obstacle2_x -= obstacle_speed
    if obstacle2_x < -300:
        obstacle2_x = random.randint(1300, 1400)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
pg.quit()