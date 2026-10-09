import kinem
from numpy import pi, sin, cos, nditer, linspace

# create RobotArm
robot = kinem.KinematicModel([1,1])

# TODO define width and height of the ellipse 
w = 
h = 
qi_list = []
n = 200
# loop from 0 to 2pi in n steps
for a in nditer(linspace(0, pi*2, n, endpoint=False)):
	# TODO calculate point on ellipse given the angle a: see https://de.wikipedia.org/wiki/Ellipse#/media/File:Elliko-sk.svg

	# TODO calculate joint positions (incl. end effector) using inverse geomtry

	# TODO add joint list to qi_list


# display the animation
robot.animate(qi_list, 10, traj=[True])