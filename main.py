import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey
from directkeys import space_pressed as sp
from game import player as p
import math
import time
import pygame as pg
import random 
#from collections import deque
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
    startscreen = pg.image.load("assets/start.png").convert()
    bg_width = bg.get_width()

    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1

    frog = p.Player((150, 450))
    player = pg.sprite.GroupSingle()
    player.add(frog)

    # always two obstacles being constantly updated 
    obstacle = pg.image.load("assets/reeds.png").convert_alpha()
    obstacle = pg.transform.rotozoom(obstacle, 0, 0.7)
    obstacle_x = 700
    obstacle_speed = 5
    obstacle2 = pg.image.load("assets/reeds.png").convert_alpha()
    obstacle2 = pg.transform.rotozoom(obstacle2, 0, 0.7)
    obstacle2_x = 1100

    detector = HandDetector(detectionCon = 0.8, maxHands = 1)

    space_key_pressed = sp

    time.sleep(2)
    current_key_pressed = set()

    video = cv2.VideoCapture(0)
    video.set(3, 640)
    video.set(4, 480)
    game_is_running = True
    screen = pg.display.set_mode((1200, 900))

    #frog_img = pygame.image.load("game/assets/froggy.png")
    #frog_img = pygame.transform.scale(frog_img, (frog_img.get_width() / 6, frog_img.get_height() / 6))
    #frog_frame = frog_img.get_rect()
    #frog_frame.center = (1200 // 6, 900 // 6)
    #reed_frames = deque()


    #creates the frame with video to detect hand
    start = True
    while True:

        if not game_is_running:
            text = pg.font.SysFont("Helveica Bold.ttf", 64).render("Game over!", True, (188, 214, 189))
            tr = text.get_rect()
            tr.center = (1200 / 2, 900 / 2)
            screen.blit(text, tr)
            pg.display.update()
            pg.time.wait(2000)
            video.release()
            cv2.destroyAllWindows()
            pg.quit()
            sys.exit()

        #imgBg = cv2.imread("game/assets/scrollbackground.png")

        ret, frame = video.read()
        keyPressed = False
        spacePressed = False
        key_count = 0
        key_pressed = 0
        hands, img = detector.findHands(frame)

        spaceevent = pg.event.Event(pg.KEYDOWN, unicode="0", key=pg.K_SPACE, mod=pg.KMOD_NONE) 
        uevent = pg.event.Event(pg.KEYDOWN, unicode="u", key=pg.K_u, mod=pg.KMOD_NONE) 
        kevent = pg.event.Event(pg.KEYDOWN, unicode="k", key=pg.K_k, mod=pg.KMOD_NONE) 

        imgScaled = cv2.resize(img, (0, 0), None, 0.533, 0.533)

        cv2.rectangle(img, (0, 480), (300, 425), (0, 0, 0), -2)
        cv2.rectangle(img, (640, 480), (300, 425), (0, 0, 0), -2)

        if hands:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    video.release()
                    cv2.destroyAllWindows()
                    pg.quit()
                    sys.exit()
            lmlist = hands[0]
            fingerUp = detector.fingersUp(lmlist)
            if fingerUp == [0, 0, 0, 0, 0]:
                cv2.putText(imgScaled, "Finger Count: 0", (0, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                cv2.putText(imgScaled, "On ground", (0, 150),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
            if fingerUp == [1, 0, 0, 0, 0]:
                cv2.putText(imgScaled, "Finger Count: 1", (0, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                cv2.putText(imgScaled, "Start game!", (0, 150),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                PressKey(0x25) #k to start game keybind
                current_key_pressed.add(0x25)
                key_pressed = True
                key_count = key_count + 1
                pg.event.post(kevent)
            if fingerUp == [1, 1, 1, 1, 1]:
                cv2.putText(imgScaled, "Finger Count: 5", (0, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                cv2.putText(imgScaled, "Jumping", (0, 150),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                PressKey(space_key_pressed) #space to jump keybind
                space_pressed = True
                pg.event.post(spaceevent) 
            if fingerUp == [0, 1, 0, 0, 0]:
                cv2.putText(imgScaled, "Finger Count: 1", (0, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                cv2.putText(imgScaled, "Diving", (0, 150),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
                PressKey(0x16)
                current_key_pressed.add(0x16)
                key_pressed = True
                key_count = key_count + 1
                pg.event.post(uevent) 
            
            if not keyPressed and len(current_key_pressed) != 0:
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
            elif key_count == 1 and len(current_key_pressed) == 2:
                for key in current_key_pressed:
                    if key_pressed != key:
                        ReleaseKey(key)
                current_key_pressed = set()
                for key in current_key_pressed:
                    ReleaseKey(key)
                current_key_pressed = set()
        cv2.imshow("Camera", imgScaled)

        clock.tick(FPS)

        if start: 
            for i in range(0, tiles):
                screen.blit(startscreen, (i * bg_width + scroll, 0))
            
            for event in pg.event.get(): 
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_k: 
                        start = False

        if not start:
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
            o_rect = screen.blit(obstacle, (obstacle_x, 320))
            obstacle_x -= obstacle_speed
            obstacle_rand = random.randint(1200, 1300)
            if obstacle_x < -300:
                obstacle_x = obstacle_rand
            o2_rect = screen.blit(obstacle2, (obstacle2_x, 320))
            obstacle2_x -= obstacle_speed
            if obstacle2_x < -300:
                obstacle2_x = obstacle_rand + 100

            # collision detection
            frog_rect = frog.rect
            if frog_rect.colliderect(o_rect) or frog_rect.colliderect(o2_rect):
                game_is_running = False

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_SPACE: 
                    if(frog.on_floor):
                        frog.jump()
                        print("space")
                if event.key == pg.K_u:
                    if(frog.on_floor):
                        frog.swimming = True 
                        frog.down()
                        print("swim")
                vertical_collision(frog)

        pg.display.update()

        k = cv2.waitKey(1)
        if k == ord("q"):
            break


#video.release()

#cv2.destroyAllWindows() 
if __name__ == '__main__': 
    main()
