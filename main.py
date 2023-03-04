import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon = 0.8, maxHands = 1)

video = cv2.VideoCapture(0)

#creates the frame with video to detect hand
while True:
    ret, frame = video.read()
    hands, img = detector.findHands(frame)
    if hands:
        lmlist = hands[0]
        fingerUp = detector.fingersUp(lmlist)
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, "Finger Count: 0", (20, 460),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, "Finger Count: 5", (20, 460),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
        if fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, "Finger Count: 2", (20, 460),cv2.FONT_HERSHEY_COMPLEX, 1, (188, 214, 189), 1, cv2.LINE_AA)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break


video.release()

cv2.destroyAllWindows() 
