import pygame as pg
import math
import player as p

clock = pg.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200 #probs should change
SCREEN_HEIGHT = 900 #probs should change

def vertical_collision(player): 
    player.update_gravity()
    print(player.rect.bottom)
    if player.rect.bottom > 875 and not player.swimming: 
        player.rect.bottom = 875
        player.direction.y = 0
        player.on_floor = True
    if player.rect.bottom > 1000 and player.swimming:
        player.swimming = False
        player.rect.bottom = 875
        player.direction.y = 0



def main():
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg = pg.image.load("assets/scrollbackground.png").convert()
    bg_width = bg.get_width()

    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

    frog = p.Player((150, 450))
    player = pg.sprite.GroupSingle()
    player.add(frog)


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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
    pg.quit()

if __name__ == '__main__':
    main()