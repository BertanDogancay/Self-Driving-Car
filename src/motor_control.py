from smbus2 import SMBus
# import ps4 as JS
# import pygame
# import time

class motor_control:

    # initialize I2C communication
    bus = SMBus(0)

    # global variables
    ADC_BAR_ADDR = 0x00
    MOTOR_TYPE_ADDR = 0x20
    MOTOR_ENCODER_POLORITY_ADDR = 0x21
    MOTOR_FIXED_PWM_ADDR = 0x31
    MOTOR_FIXED_SPEED_ADDR = 0x51
    MOTOR_ENCODER_TOTAL_ADDR = 0x60
    CONTROLLER_ADDRESS = 0x34

    # Motor position addresses for controller
    MOTOR_FRONT_LEFT = 0x34
    MOTOR_FRONT_RIGHT = 0x33
    MOTOR_BACK_LEFT = 0x36
    MOTOR_BACK_RIGHT = 0x35

    speed = None

    def send_command(self, motorType, speed):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, motorType, speed)

    def move_forward(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, self.speed)

    def move_backwards(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, -self.speed)

    def move_right(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, -self.speed)

    def move_left(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, self.speed)

    def move_diagonal_right(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, 0)

    def move_diagonal_left(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, self.speed)

    def turn_right(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, self.speed)

    def turn_left(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, 0)

    def turn_around(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, -self.speed)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, self.speed)

    def stop(self):
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x33, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x34, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x35, 0)
        self.bus.write_byte_data(self.CONTROLLER_ADDRESS, 0x36, 0)

# if __name__ == '__main__':

#     pygame.init()

#     motor = motor_control()
#     motor.speed = 30

#     enable = 1

#     while True:
#         jsVal = JS.getJS()

#         if jsVal['axis2'] < -0.90:
#             motor.move_forward()
#             enable = 0
#             print("Moving Forward")
#             print(enable)
#         elif jsVal['axis2'] > 0.90:
#             motor.move_backwards()
#             enable = 0
#             print("Moving Backwards")
#         elif jsVal['axis1'] < -0.90:
#             motor.move_left()
#             enable = 0
#             print("Moving Left")
#         elif jsVal['axis1'] > 0.90:
#             motor.move_right()
#             enable = 0
#             print("Moving Right")
#         elif jsVal['axis1'] > 0.50 and jsVal['axis2'] < -0.50:
#             motor.move_diagonal_right()
#             enable = 0
#             print("Moving Diagonal Right")
#         elif jsVal['axis1'] < -0.50 and jsVal['axis2'] > 0.50:
#             motor.move_diagonal_left()
#             enable = 0
#             print("Moving Diagonal Left")
#         elif jsVal['R2']:
#             motor.turn_right()
#             enable = 0
#             print("Turning Right")
#         elif jsVal['L2']:
#             motor.turn_left()
#             enable = 0
#             print("Turning Left")
#         elif jsVal['o']:
#             motor.stop()
#             print("Stopping")
#         time.sleep(0.1)

#     while True:
#         val = input()
#         print(val)
#         if val == '1':
#             motor.move_forward()
#         if val == '2':
#             motor.move_backwards()
#         if val == '3':
#             motor.move_diagonal_right()
#         if val == '4':
#             motor.move_diagonal_left()
#         if val == '5':
#             motor.turn_right()
#         if val == '6':
#             motor.turn_left()
#         if val == '7':
#             motor.turn_around()
#         if val == 'x':
#             motor.stop()