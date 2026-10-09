import numpy as np
import kinem
from numpy import pi, sin, cos, dot
import myRobotArm as my

# create RobotArm, now with 3 arm links
robot = my.RobotArm([1, 1, 0.2])

# TODO define line length as 2 and corner radius as 0.5
a = 
r = 

qi_list = []

# TODO set the velocity to 0.02
speed = 

# TODO set starting position to lower tight corner at the beginning of the straight
# line segment
qi = 
qi_list.append(qi[:])

# helper function to draw a line with velocityvector dP
def line(dP):
    # use global variables
    global a, speed, qi_list, qi
    # calculate x steps depending on the line length (a) and the velocity
    for t in np.nditer(np.linspace(0, a, a/speed, endpoint=True)):
        # TODO calculate angular vleocities using the jacobian
  

        # TODO add angular velocities to joint angles


# helper function to draw a circle segment from angle a1 to angle a2
def circle(a1, a2):
    # use global variables
    global r, speed, qi_list, qi
    # calculate x steps depending on the line length (a) and the velocity
    for a in np.nditer(np.linspace(a1, a2, pi/4/speed, endpoint=True)):
        # calculate velocity vector
        dP = [-sin(a)*speed, cos(a)*speed, speed*2]

        # TODO calculate angular vleocities using the jacobian

        # TODO add angular velocities to joint angles


# calculate lines and arcs
line([0, speed, 0])
circle(0, pi/2)
line([-speed, 0, 0])
circle(pi/2, pi)
line([0, -speed, 0])
circle(pi, pi*1.5)
line([speed, 0, 0])
circle(pi*1.5, pi*2)

# display the animation
robot.animate(qi_list, 10, traj=[True])