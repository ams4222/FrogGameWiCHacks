import pygame as pg
import math

clock = pg.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200 #probs should change
SCREEN_HEIGHT = 900 #probs should change

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg = pg.image.load("assets/scrollbackground.png").convert()
bg_width = bg.get_width()

scroll = 0
tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

run = True
while run:
    clock.tick(FPS)

    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    scroll -= 5

    if abs(scroll) > bg_width:
        scroll = 0

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.display.update()
pg.quit()