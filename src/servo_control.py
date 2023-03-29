import board
import busio
from adafruit_servokit import ServoKit
import adafruit_pca9685
from time import sleep
import ps4 as JS
import pygame

pygame.init()

i2c = busio.I2C(board.SCL, board.SDA)
pwm = adafruit_pca9685.PCA9685(i2c)
pwm.frequency = 50
pwm = ServoKit(channels=16)

pwm.servo[0].angle = 0
print("servo1 good")
sleep(5)
pwm.servo[1].angle = 0
print("servo2 good")

count1 = 0
count2 = 0

while True:
    jsVal = JS.getJS()

    if jsVal['axis1'] > 0.50 and count1 < 180:
        count1 += 1
        print(count1)
    elif jsVal['axis1'] < -0.50 and count1 > 0:
        count1 -= 1
        print(count1)
    if jsVal['axis4'] < -0.50 and count2 < 180:
        count2 += 1
        print(count2)
    elif jsVal['axis4'] > 0.50 and count2 > 0:
        count2 -= 1
        print(count2)

    pwm.servo[0].angle = count1
    pwm.servo[1].angle = count2
    sleep(0.005)