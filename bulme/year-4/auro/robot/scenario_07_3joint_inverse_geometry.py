import numpy as np
import kinem
from numpy import pi, sin, cos, dot
import myRobotArm as my

# create RobotArm, now with 3 arm links
robot = my.RobotArm([1, 1, 0.2])

# TODO calculate joint angles to reach 1, 1 with angle 0 using inverse geometry


# draw robot arm with calculated joint angles
Pi = robot.directGeometry(qi)
robot.plot(Pi, ref=0.3)