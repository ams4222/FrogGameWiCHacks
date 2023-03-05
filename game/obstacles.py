import pygame as pg
from player import *
import random

class Obstacle(pg.sprite.Sprite):
    def __init__(self, obstacle_x, obstacle2_x, pos):
        super().__init__()
        # later, randomize 
        self.image = pg.image.load("assets/froggy.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.obstacle_x = obstacle_x
        self.obstacle2_x = obstacle2_x
    
    def update(self, shift_x):
        self.rect.x -= shift_x
        if(abs(self.obstacle_x - self.obstacle2_x) < 200):
            self.obstacle2_x += 150
        obstacle_rand = random.randint(1200, 1300)
        if self.obstacle_x < -300:
            self.obstacle_x = obstacle_rand
        if self.obstacle2_x < -300:
            self.obstacle2_x = obstacle_rand + 100
'''
class Cactus(pygame.sprite.Sprite):
    def __init__(self, speed=5, sx=-1, sy=-1):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.imgs, self.rect = load_sprite_sheet('cactus-small.png', 3, 1, sx, sy, -1)
        self.rect.bottom = int(0.98 * height_screen)
        self.rect.left = width_screen + self.rect.width
        self.image = self.imgs[random.randrange(0, 3)]
        self.movement = [-1*speed,0]

    def draw(self):
        screenDisplay.blit(self.image, self.rect)

    def update(self):
        self.rect = self.rect.move(self.movement)

        if self.rect.right < 0:
            self.kill()
'''