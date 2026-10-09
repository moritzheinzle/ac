import numpy as np
import kinem
from numpy import pi, sin, cos, dot
import myRobotArm as my

# create RobotArm, now with 3 arm links
robot = my.RobotArm([1, 1, 0.2])

# TODO set start and end point - draw a horizontal line
P1 = 
P2 = 

qi_list = []
n = 100
# loop from 0 to 2 in n steps
for t in np.nditer(np.linspace(0, 2, n, endpoint=False)):
    # calculate s to go from 0 to 1 and back to 0 so the animatino can loop
    s = t if t < 1 else 2-t
    # calculate current target P
    P = np.add(dot(P1, 1-s), dot(P2, s))
    
    # TODO calculate joint angles for target P and constant angle pi/2 using inverse geometry
    
    # TODO add joint angles to list
    

# display the animation
robot.animate(qi_list, 10, traj=[True], ref=0.2)