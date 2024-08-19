from picamera2 import Picamera2
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.FPS import FPS

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'format': 'RGB888', 'size': (288,288)}))
picam2.start()

fpsReader = FPS(avgCount=30)

detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

while True:
    img = picam2.capture_array()
    fps, img = fpsReader.update(img, pos=(20, 20), bgColor=(0, 200, 0), textColor=(255, 255, 255), scale=0.8, thickness=2)
    hands, img = detector.findHands(img, draw=True, flipType=True)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        center1 = hand1['center'] 
        handType1 = hand1["type"]
        fingers1 = detector.fingersUp(hand1)
        print(f'H1 = {fingers1.count(1)}', end=" ")
        length, info, img = detector.findDistance(lmList1[8][0:2], lmList1[12][0:2], img, color=(255, 0, 255), scale=10)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            center2 = hand2['center']
            handType2 = hand2["type"]
            fingers2 = detector.fingersUp(hand2)
            print(f'H2 = {fingers2.count(1)}', end=" ")
            length, info, img = detector.findDistance(lmList1[8][0:2], lmList2[8][0:2], img, color=(255, 0, 0), scale=10)
        print(" ")

    cv2.imshow("Image", img)
    cv2.waitKey(1)
