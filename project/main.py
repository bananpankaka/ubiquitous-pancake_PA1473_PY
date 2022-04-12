#!/usr/bin/env pybricks-micropython
import sys
import __init__ #je ne sais pas?

from pybricks.ev3devices import Motor, ColorSensor #definierat motorn genom att läsa dokumentationen rad 5-8
from pybricks.parameters import Port, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

lift = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears=[12, 36]) #lyften, måtten är måtten på 

left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears = [12, 20])
right_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears = [12, 20])


bobbe = DriveBase(left_motor, right_motor, wheel_diameter = 47, axel_track = 120)

def main():

    bobbe.straight(100) #100=100millimeter
    #lift.run_untill_stalled(50, then = Stop.HOLD, duty_limit = 60)

    print("Im done")

    return 0

if __name__ == '__main__':
    sys.exit(main())

#settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
#viktig grej


hallåhallå