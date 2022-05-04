#!/usr/bin/env pybricks-micropython

import sys
from time import *

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Direction, Button, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# Initialize the EV3 hub
hub = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.C, positive_direction = Direction.COUNTERCLOCKWISE, gears = [12 , 20])
right_motor = Motor(Port.B, positive_direction = Direction.COUNTERCLOCKWISE, gears = [12, 20])
fork_motor = Motor(Port.A, positive_direction = Direction.CLOCKWISE, gears = [14, 36])

# Initialize the sensors.
line_sensor = ColorSensor(Port.S3)
pallet_sensor = TouchSensor(Port.S1)


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter= 47, axle_track= 128)

def read_pressed_button():
    while 1:
        button_list = hub.buttons.pressed()
        if not button_list == []:
            hub.speaker.beep()
            sleep(1)
            return button_list[0]

def read_reflection():
    return line_sensor.reflection()

def line_following():

    # When the DOWN button is pressed, the line reflection value is stored in the line_reflection variable
    if read_pressed_button() == Button.DOWN:
        line_reflection = read_reflection()
    
    if read_pressed_button() == Button.UP:
        background_reflection = read_reflection()
    
    threshold = (background_reflection + line_reflection)/2

    DriveSpeed = 30
    PROPORTIONAL_GAIN = 1.2
    
    while True:
        
        deviation = line_sensor.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DriveSpeed, turn_rate)
    
    return 0

def hit_pallet():
    
    if pallet_sensor.pressed():
        return True
    else: 
        return False


def pick_up_pallet():

    # Reset arms: Move arms to ground
    fork_motor.run_until_stalled(90, then = Stop.HOLD)
    sleep(1)
    fork_motor.reset_angle(0)
    sleep(1)
    while not hit_pallet():
        robot.drive(30, 0)
    # Lift pallet
    #robot.stop()
    fork_motor.run_angle(-420, 130)
    if not pallet_sensor.pressed():
        robot.stop()



def main():
    pick_up_pallet()
    return 0

if __name__ == '__main__':
    sys.exit(main())

#settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
#viktig grej