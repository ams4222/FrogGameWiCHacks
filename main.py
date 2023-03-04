import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detectionCon = 0.8, maxHands = 1)

video = cv2.VideoCapture(0)

#creates the frame with video to detect hand
while True:
    ret, frame = video.read()
    hands, img = detector.findHands(frame)
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break


video.release()
cv2.destroyAllWindows() 
