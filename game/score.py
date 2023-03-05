import pygame as pg

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

def extractDigits(num):
    if num > -1:
        d = []
        i = 0
    while(num / 10 != 0):
        d.append(num % 10)
        num = int(num / 10)

    d.append(num % 10)
    for i in range(len(d),5):
        d.append(0)
    d.reverse()
    return d

class Scoreboard():
    def __init__(self, x = 1, y = 1):
        self.score = 0
        self.score_img, self.scorerect = pg.load_sprite_sheet("FILEPATH", 12, 1, 11, int(11 * 6 / 5), -1)
        self.image = pg.Surface((55, int(11 * 6 / 5)))
        self.rect = self.image.get_rect()
        
        if x == -1:
            self.rect.left = SCREEN_WIDTH * 0.89
        else:
            self.rect.left = x
        
        if y == -1:
            self.rect.top = SCREEN_HEIGHT * 0.1
        else:
            self.rect.top = y

    def draw(self):
        screen.blit(self.image, self.rect)
    
    def update(self, score):
        score_digits = extractDigits(score)
        self.image.fill(backgroundColor)
        for s in score_digits:
            self.image.blit(self.scre_img[s], self.screrect)
            self.screrect.left += self.screrect.width
        self.screrect.left = 0