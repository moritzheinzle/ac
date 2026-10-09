import kinem
from numpy import pi

#TODO:

# create RobotArm
robot = kinem.KinematicModel([1,1])  

# define joint angles
q1 = 0 
q2 = pi/4

# calculate joint positions (incl. end effector)
Pi = robot.directGeometry([q1,q2]) 
# draw robot with referential frame with axis length of 0.3
robot.plot(Pi, ref=0.3)
