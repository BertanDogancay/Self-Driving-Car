import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone
import board
import busio
from adafruit_servokit import ServoKit
import time

i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_pca9685

pwm = adafruit_pca9685.PCA9685(i2c)
pwm.frequency = 50
pwm = ServoKit(channels=16)

pwm.servo[0].angle = 45
print("SERVO 1/2 READY")
time.sleep(5)
pwm.servo[1].angle = 100
print("SERVO 2/2 READY")
 
# Webcam
cap = cv2.VideoCapture(0)
_, frame = cap.read()
rows, cols, _ = frame.shape
# cap.set(3, 1280)
# cap.set(4, 720)

x_medium = int(cols / 2)
y_medium = int(cols / 2)
center = int(cols / 2)

positionX = 45
positionY = 100
 
# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)
 
# Find Function
# x is the raw distance y is the value in cm
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C
 
# Loop
while True:
    success, img = cap.read()
    hands = detector.findHands(img, draw=False)
 
    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        x1, y1, _ = lmList[5]
        x2, y2, _ = lmList[17]

        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
 
        distance = int(math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))
        A, B, C = coff
        distanceCM = A * distance ** 2 + B * distance + C
 
        # print(distanceCM, distance)
 
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x+5, y-10))

        cv2.line(img, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
        cv2.line(img, (0, y_medium), (750, y_medium), (0, 255, 0), 2)
 
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == 27:
        break

    if x_medium < center -70:
        positionX += 2
    elif y_medium > center +70:
        positionY += 2
    elif x_medium > center +70:
        positionX -= 2
    elif y_medium < center -70:
        positionY -= 2

    if positionX >= 180:
        positionX -= 2
    elif positionX <= 0:
        positionX += 2

    if positionY >= 180:
        positionY -= 2
    elif positionY <= 0:
        positionY += 2 

    pwm.servo[0].angle = positionX
    pwm.servo[1].angle = positionY

cap.release()
cv2.destroyAllWindows()