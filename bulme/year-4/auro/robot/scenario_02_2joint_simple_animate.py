import kinem
from numpy import pi, linspace, nditer

# create RobotArm
robot = kinem.KinematicModel([1,1])

# create an empty list for storing the joint angles for each animation frame
qi_list = []
n = 200
# loop from 0 to 2pi in n (200) steps
# endpoint = 2pi is excluded, else when looping there would be a duplicate
# frame (2pi == 0)
for a in nditer(linspace(0, pi*2, n, endpoint=False)):
	# append a list of joint angles to qi_list
	qi_list.append([a, a*1])

# display the animation with 10ms between two frames and including the
# trajectories of P3 and P2 (the trajectories will not be cleared after
# each loop)
robot.animate(qi_list, 10, ref=0.3, traj=[True, True], traj_clear=False)
