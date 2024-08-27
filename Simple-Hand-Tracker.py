import mediapipe
import cv2
from picamera2 import Picamera2

drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main = {'format': 'RGB888', 'size': (480,360)}))
picam2.start()

with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:

     while True:
           frame1 = picam2.capture_array()
           
           results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
           
           if results.multi_hand_landmarks != None:
              for handLandmarks in results.multi_hand_landmarks:
                  drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                  
                  for point in handsModule.HandLandmark:
                      normalizedLandmark = handLandmarks.landmark[point]
                      pixelCoordinatesLandmark= drawingModule._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, 640, 480)
                      if point == 8:
                          print(point)
                          print(pixelCoordinatesLandmark)
                          print(normalizedLandmark)

           cv2.imshow("Frame", frame1);
           key = cv2.waitKey(1) & 0xFF

           if key == ord("q"):
              break
