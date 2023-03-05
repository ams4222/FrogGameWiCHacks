import sys
import cv2
from cvzone.HandTrackingModule import HandDetector
from directkeys import PressKey, ReleaseKey
from directkeys import space_pressed
import time
import pygame as pg
#from collections import deque

detector = HandDetector(detectionCon = 0.8, maxHands = 1)

space_key_pressed = space_pressed

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

    imgBg = cv2.imread("game/assets/scrollbackground.png")

    ret, frame = video.read()
    keyPressed = False
    spacePressed = False
    key_count = 0
    key_pressed = 0
    hands, img = detector.findHands(frame)

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
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(imgScaled, "Finger Count: 5", (0, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
            cv2.putText(imgScaled, "Jumping", (0, 150),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
            PressKey(space_key_pressed) #space to jump keybind
            space_pressed = True
            current_key_pressed.add(space_key_pressed)
            key_pressed = space_key_pressed
            key_pressed = True
            key_count = key_count + 1
        if fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(imgScaled, "Finger Count: 1", (0, 200),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
            cv2.putText(imgScaled, "Diving", (0, 150),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
            PressKey(0x16)
            current_key_pressed.add(0x16)
            key_pressed = True
            key_count = key_count + 1
         
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

    cv2.imshow("Hoppy Hand", imgBg)
    cv2.imshow("Camera", imgScaled)

    k = cv2.waitKey(1)
    if k == ord("q"):
        break


#video.release()

#cv2.destroyAllWindows() 
