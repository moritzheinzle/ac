import kinem
import numpy as np
from numpy import pi, sin, cos, dot, sqrt, arctan2, arccos


class RobotArm(kinem.KinematicModel):
    def directGeometry(self, qi):
        l1, l2, l3 = self.l
        q1, q2, q3 = qi

        T1_0 = np.array([[cos(q1), -sin(q1), 0, 0],
                         [sin(q1),  cos(q1), 0, 0],
                         [      0,        0, 1, 0],
                         [      0,        0, 0, 1]
                         ]) 
        # Homogenous transformation from 2 to 1
        T2_1 = np.array([[cos(q2), -sin(q2), 0, l1],
                         [sin(q2),  cos(q2), 0, 0],
                         [      0,        0, 1, 0],
                         [      0,        0, 0, 1]
                         ])
        T3_2 = np.array([[cos(q3), -sin(q3), 0, l2],
                         [sin(q3),  cos(q3), 0, 0],
                         [      0,        0, 1, 0],
                         [      0,        0, 0, 1]
                         ]) 
        # Homogenous transformation from 3 to 2
        T4_3 = np.array([[1, 0, 0, l3],
                         [0, 1, 0, 0 ],
                         [0, 0, 1, 0 ],
                         [0, 0, 0, 1 ]
                         ])

        T2_0 = dot(T1_0, T2_1)
        T3_0 = dot(T2_0, T3_2)
        T4_0 = dot(T3_0, T4_3)

        x2 = T2_0[0, 3]
        y2 = T2_0[1, 3]
        x3 = T3_0[0, 3]
        y3 = T3_0[1, 3]
        x4 = T4_0[0, 3]
        y4 = T4_0[1, 3]


        P1 = np.array([0, 0])
        P2 = np.array([x2, y2])
        P3 = np.array([x3, y3])
        P4 = np.array([x4, y4])

        return [P1, P2, P3, P4]

    
    def inverseGeometry(self, x, y, alpha = None):
        l1, l2, l3 = self.l
        # when no alpha, set it to the angle of the vector from origin to
        # target
        if alpha == None:
            alpha = arctan2(y, x)

        # TODO calculate new target(x, y) depending on alpha
        
        
        # TODO use inverse geometric approach 
        return ([0,0,0])
    

    def jacobian(self, qi):
        l1, l2, l3 = self.l
        q1, q2, q3 = qi

        #TODO calculate jacobian for 3 joints
        

        return np.array([
            [0, 0, 0],
            [0, 0, 0],
            [  0,   0,   0]
        ])
