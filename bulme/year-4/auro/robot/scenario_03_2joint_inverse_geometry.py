import kinem

# create RobotArm
robot = kinem.KinematicModel([1,1])

# TODO calculate joint angles for a target point 1.5,1 using inverse geometry
qi = 

# calculate joint positions (incl. end effector)
Pi = robot.directGeometry(qi)
# draw robot with referential frame with axis length of 0.3
robot.plot(Pi, ref=0.3)