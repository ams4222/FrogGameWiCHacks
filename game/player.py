import pygame as pg 
tile_size = 64
screen_width = 1200
screen_height = 900 

class Player(pg.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        #creates a list of all images used for animation
        #resizes all images to correct tile size

        self.sprites = []
        size = (64, 64)
        self.sprites.append(pg.transform.scale(pg.image.load('assets/froggy.png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('assets/froggy.png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('assets/froggy.png'), size))
        self.sprites.append(pg.transform.scale(pg.image.load('assets/froggy.png'), size))
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        #loads idle image and makes sure the player is touching ground

        self.image = pg.image.load("assets/froggy.png").convert_alpha()
        #((tile_size/2)/14)
        self.image = pg.transform.rotozoom(self.image, 0, 0.5)
        self.rect = self.image.get_rect(topleft = pos)

        # direction has both x and y

        self.direction = pg.math.Vector2()
        self.speed = pg.math.Vector2()
        self.speed.x = 6
        self.speed.y = 6
        self.gravity = 0.5
        self.jump_speed = -16

        self.on_floor = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.is_animating = False

        #status of player for animation

        self.facing_right = True
        self.swimming = False

        #function for animations based on player movement

    def get_status(self):
        if self.direction.y < 0:
            self.status = self.animate()
        elif self.direction.y > 1:
            self.status = self.animate()
        else:
            if self.direction.x != 0:
                self.status = self.animate()
            else:
                self.status = 'assets/froggy.png'
        

    #animation function that makes sure it is always animating

    def animate(self):
        self.is_animating = True

    #movement based on keys being pressed

    def key_input(self):
        keys = pg.key.get_pressed()
        self.direction.x = 0
        if keys[pg.K_SPACE]:
            if(self.on_floor):
                 self.jump()
            pass
        if keys[pg.K_u]:
            self.swimming = True
            if(self.on_floor):
                self.down()
    
    #gravity for player

    def update_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed 
        self.gravity = 0.5
    
    def down(self):
        self.direction.y = -self.jump_speed 
        self.gravity = -0.5

    #update function that implements all above functions to properly run the player class

    def update(self):
        #self.key_input()
        if self.direction.x and self.direction.y != 0:
           self.is_animating == True
           self.current_sprite += 0.8

           if self.current_sprite >= len(self.sprites):
              self.current_sprite = 0
              self.is_animating = False
        else:
            self.is_animating = False
            self.status = 'assets/froggy.png'

            self.image = self.sprites[int(self.current_sprite)]
        self.animate()
