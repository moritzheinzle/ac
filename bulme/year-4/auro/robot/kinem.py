import numpy as np
import matplotlib.pyplot as plt
import geom
from numpy import sin, cos

#-------------------------------------------------------------------------------
# The KinematicModel extends the GeometricModel by functions used for 
# kinematics.
# 
class KinematicModel(geom.GeometricModel):
    #---------------------------------------------------------------------------
    # jacobian(qi)
    #
    # Takes a list of joint angles (in radians) and returns the corresponding
    # jacobian matrix.
    #
    # arguments:
    #   qi ... list of angles [q1, q2, ...]
    #
    # returns jacobian matrix (numpy array)
    #
    def jacobian(self, qi):
        l1, l2 = self.l
        q1, q2 = qi

        #TODO calculate the Jacobian matrix J; hint: use np.sin and np.cos
        dummyJ = np.array([
            [0, 0],
            [0, 0],
            [  0,   0]
        ])
        return dummyJ