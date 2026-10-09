import numpy as np
import kinem
from numpy import sin, cos, pi, arctan2, tan

# create RobotArm
robot = kinem.KinematicModel([1,1])

# define width and height of the ellipse, why can't w be 2?
w = 1.9
h = 1
# TODO calculate joint angles of starting position


n = 200
# loop from 0 to 2pi in n steps
for a in np.nditer(np.linspace(0, pi*2, n, endpoint=False)):
    # TODO calculate jacobian for given angles
 
    # TODO make jacobian squared by removing angular velocity

    # check, that determinant is not zero (-> J can be inverted)
    det = np.linalg.det(J)
    if det == 0:
        print("det 0!")
    else:
        # approximate arc length with the length of two adjecent
        # points
        P = [cos(a) * w, sin(a) * h]
        da = pi*2/n
        P2 = [cos(a + da) * w, sin(a + da) * h]
        # calculate tangent vector and scale to approximated arc length
        dP = [-sin(a) * w, cos(a) * h]
        dP = np.divide(dP, np.linalg.norm(dP))
        length = np.linalg.norm(np.subtract(P2, P))
        dP = np.dot(dP, length)

        #TODO  get the inverse of the jacobian
        
        # TODO calculate angular velocity
        

        # TODO add angular velocities to joint angles
        
        # TODO store copy! of current joint angles in qi_list; a copy is needed because qi is modified each step
      

# display the animation
robot.animate(qi_list, 10, traj=[True])