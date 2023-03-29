import cv2
import board
import busio
import numpy as np
from adafruit_servokit import ServoKit
from flask import Flask, render_template, Response
import adafruit_pca9685
import time

app = Flask(__name__)

i2c = busio.I2C(board.SCL, board.SDA)

pwm = adafruit_pca9685.PCA9685(i2c)
pwm.frequency = 50
pwm = ServoKit(channels=16)

pwm.servo[0].angle = 45
print("SERVO 1/2 READY")
time.sleep(5)
pwm.servo[1].angle = 100
print("SERVO 2/2 READY")

cap = cv2.VideoCapture(0)
_, img = cap.read()
rows, cols, _ = img.shape

x_medium = int(cols / 2)
y_medium = int(cols / 2)
center = int(cols / 2)

positionX = 45
positionY = 100

while True:
    _, img = cap.read()

    cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
    hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)

        x_medium = int((x + x + w) / 2)
        y_medium = int((y + y + h) / 2)
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        break

    cv2.line(img, (x_medium, 0), (x_medium, 480), (0, 255, 0), 2)
    cv2.line(img, (0, y_medium), (750, y_medium), (0, 255, 0), 2)

    cv2.imshow("Frame", img)

    key = cv2.waitKey(1)    

    if key == 27:
        break

    if x_medium < center -70:
        positionX += 3
    elif y_medium > center +70:
        positionY += 3
    elif x_medium > center +70:
        positionX -= 3
    elif y_medium < center -70:
        positionY -= 3

    if positionX >= 180:
        positionX -= 3
    elif positionX <= 0:
        positionX += 3

    if positionY >= 180:
        positionY -= 3
    elif positionY <= 0:
        positionY += 3 

    pwm.servo[0].angle = positionX
    pwm.servo[1].angle = positionY

cap.release()
cv2.destroyAllWindows()