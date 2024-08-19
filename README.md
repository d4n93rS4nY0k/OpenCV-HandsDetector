
# OpenCV Hands Detector

The project is based on Raspberry Pi 4 and RPicameraV2

Used programming languages: Python (100%)


## Used Libraries

Necessary libraries for working with source code:

**Picamera2 0.3.18 (or newer)**
```bash
  pip install picamera2
```

**CVzone 1.6.1 (or newer)**
```bash
  pip install cvzone
```

**OpenCV 4.10.0.84 (or newer)**
```bash
  pip install opencv-python
```

Make sure that all libraries have been installed **correctly**:

Open terminal. Run commands:
```bash
  python

  import cv2

  import cvzone
```

## Picamera2 verification

Run a simple example **testopencamera.py** to see if the picamera2 works great

```python
import cv2
from picamera2 import Picamera2

cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main = {'format': 'XRGB8888', 'size': (640, 480)}))
picam2.start()

while True:
	im = picam2.capture_array()
	cv2.imshow('camera', im)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
```
## Code explanation

- **Libraries import section**
Importing: *cv2*, *cvzone* and some sub-libraries from *cvzone*.
```python
from picamera2 import Picamera2
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from cvzone.FPS import FPS
```
- **Camera initialization**
Configuration of the camera image format and its resolution.

Camera startup and hands detection, fps counter function imported from the library.
```python
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={'format': 'RGB888', 'size': (288,288)}))
picam2.start()

fpsReader = FPS(avgCount=30)

detector = HandDetector(staticMode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)
```
- **Main while True loop**
```python
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
```



## Viewers count

![Visitor Count](https://profile-counter.glitch.me/d4n93rS4nY0k/count.svg)



## Authors

- [@d4n93rS4nY0k](https://github.com/d4n93rS4nY0k)

