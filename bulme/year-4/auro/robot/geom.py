import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from numpy import pi, sin, cos, sqrt, dot, arccos, arctan2

#-------------------------------------------------------------------------------
# The GeometricModel is a geometrical description of a kinematic system.
# It provides not only functions to calculate the direct and inverse geometrical
# approach, but also plot and animate functions.
# 
class GeometricModel(object):
    #---------------------------------------------------------------------------
    # GeometricModel(li)
    # 
    # The constructor takes a list of the length of the elements.
    # The unit of length is not specified, use whatever you want.
    #
    # arguments:
    #   li ... list of arm lengths [l1, l2, ...]
    #
    # returns an instance of the class
    #
    def __init__(self, li):
        self.l = li


    #---------------------------------------------------------------------------
    # directGeometry(qi)
    #
    # Takes a list of joint angles (in radians) and returns a list of the 
    # positions of the joints.
    #
    # arguments:
    #   qi ... list of angles [q1, q2, ...]
    #
    # returns list of points [P1, P2, ...]
    #
    def directGeometry(self, qi):
        l1, l2 = self.l
        q1, q2 = qi
        

        
        # Homogenous transformation from 1 to 0
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
        # Homogenous transformation from 3 to 2
        T3_2 = np.array([[1, 0, 0, l2],
                         [0, 1, 0, 0 ],
                         [0, 0, 1, 0 ],
                         [0, 0, 0, 1 ]
                         ])
        #TODO Homogenous transformation from 3 to 0; use dot
        T2_0 = dot(T1_0, T2_1)
        T3_0 = dot(T2_0, T3_2)

        # TODO get joint positions from transformation matrices
        x2 = T2_0[0, 3]
        y2 = T2_0[1, 3]
        x3 = T3_0[0, 3]
        y3 = T3_0[1, 3]

        P1 = np.array([0, 0])
        P2 = np.array([x2, y2])
        P3 = np.array([x3, y3])
        return [P1, P2, P3]


    #---------------------------------------------------------------------------
    # inverseGeometry(x, y, alpha = None)
    #
    # Takes the target position of the end effector and optionally the angle of
    # the end effector and returns a list of joint angles needed to reach the
    # position.
    # Throws an exception when the target cannot be reached.
    # Note: A 2 joint arm will not be able to choose a final angle, therefore
    # the parameter is only relevant for 3 or more joints.
    #
    # arguments:
    #   x ... the x position of the end effector
    #   y ... the y position of the end effector
    #   alpha ... <optional> the angle of the end effector
    #
    # returns list of angles [q1, q2, ...]
    #
    def inverseGeometry(self, x, y, alpha = None):
        l1, l2 = self.l

        #TODO calculate l, q1 and q2 (according to your paper&pencil exercise)
		#hints: ensure that you don't have a division by zero; use the arctan2 function instead of arctan

        return [0,0]
        


    #---------------------------------------------------------------------------
    # plot(Pi, ref = None)
    #
    # Displays a representation of the arm, defined by the positions of the 
    # joints, in a window.
    # If ref is set to a length, a referential frame (with axis of specified 
    # length) will be displayed for each joint.
    # Note: The joint positions can be calculated using the directGeometry
    # function.
    #
    # arguments:
    #   Pi ... list of positions [P1, P2, ...]
    #   ref ... <optional> the lenght of the axis of the referential frames
    #
    # returns nothing
    #
    def plot(self, Pi, ref = None):
        max_dim = sum(self.l)
        n = len(Pi)

        # create plot window
        plt.figure(1)
        plt.axis("equal")
        plt.axis([-max_dim, max_dim, -max_dim, max_dim])
        plt.grid(True)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Robot Arm")
        
        # draw lines
        for i in range(0, n-1):
            x1 = Pi[i][0]
            y1 = Pi[i][1]
            x2 = Pi[i+1][0]
            y2 = Pi[i+1][1]
            plt.plot([x1,x2], [y1,y2], "b", linewidth=5)

        # draw referential frames
        if ref != None:
            l = ref
            for i in range(0, n-1):
                P1 = Pi[i]
                P2 = Pi[i+1]
                x = np.subtract(P2, P1)
                x = x / np.linalg.norm(x) * l
                y = [-x[1], x[0]]
                plt.plot([P1[0], P1[0] + x[0]], [P1[1], P1[1] + x[1]], "r", linewidth=2)
                plt.plot([P1[0] + y[0], P1[0]], [P1[1] + y[1], P1[1]], "g", linewidth=2)
        
        # draw joints
        for i in range(0, n-1):
            x1 = Pi[i][0]
            y1 = Pi[i][1]
            plt.plot(x1, y1, "ko")

        # show the final plot
        plt.show()


    #---------------------------------------------------------------------------
    # animateSimple(qi_start, qi_end, steps, interval, traj = [], ref = None,
    #               traj_clear = True)
    #
    # This function is a wrapper around animate(...) to display a simple 
    # animation given the starting and ending angles of the joints.
    # For further explanation of the arguments look up animate(...).
    # Throws an exception if qi_start and qi_end do not have the same number of
    # elements.
    #
    # arguments:
    #   qi_start ... list of starting angles [q1_start, q2_start, ...]
    #   qi_start ... list of final angles [q1_end, q2_end, ...]
    #   steps ... number of steps the animation consists of (more = smoother)
    #   ... goto animate(...)
    #
    # returns nothing
    #
    def animateSimple(self, qi_start, qi_end, steps, interval, traj = [], ref = None, traj_clear = True):
        if len(qi_start) != len(qi_end):
            raise Exception("number of starting angles has to match number of final angles")
        qs = [
            np.linspace(qi_start[i], qi_end[i], steps, endpoint=False) for i in range(len(qi_start))
        ]
        self.animate(np.transpose(qs), interval, traj, ref, traj_clear)


    #---------------------------------------------------------------------------
    # animateSimple(qi_list, interval, traj = [], ref = None, traj_clear = True)
    #
    # Displays the animation of the arm using a list of lists of joint angles
    # for each step.
    # Note: the parameters can be in arbitrary order as long as they are 
    # accessed by name (animateSimple(qi_list, 10, ref = 0.3, traj = [True])).
    #
    # arguments:
    #   qi_list ... list of list of joint angles [[q1[0], q2[0], ...], 
    #                                             [q1[1], q2[1], ...], 
    #                                                      ...       ]
    #   interval ... delay in ms between two steps
    #   traj ... <optional> list of boolean [True, False, ...]. The trajectory 
    #               is drawn if the value is True for the given point (joint + 
    #               end effector) starting from the end effector. Defaults to
    #               False for each not defined point.
    #   ref ... <optional> the lenght of the axis of the referential frames
    #   traj_clear ... <default True> when True, clears the trajectories after 
    #                   the animation
    #
    # returns nothing
    #
    def animate(self, qi_list, interval, traj = [], ref = None, traj_clear = True):
        max_dim = sum(self.l)
        n = len(qi_list)
        
        # create window
        fig = plt.figure(1)
        plt.axis("equal")
        plt.axis([-max_dim, max_dim, -max_dim, max_dim])
        plt.grid(True)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Robot Arm")

        # init trajectories
        trajs = []
        for i in range(len(traj)):
            tr, = plt.plot([], [], "k-", linewidth=2)
            tr.set_data([], [])
            trajs.append(tr)

        # init lines and joints
        lines, = plt.plot([], [], "b", linewidth=5)
        joints, = plt.plot([], [], "ko")

        # init the referential frames
        refx = []
        refy = []
        l = ref
        if ref != None:
            for i in range(len(self.l)):
                ref, = plt.plot([], [], "r", linewidth=2)
                refx.append(ref)
                ref, = plt.plot([], [], "g", linewidth=2)
                refy.append(ref)

        # called at the start of each animation loop
        def init():
            # reset all lines and points
            lines.set_data([], [])
            joints.set_data([], [])
            for ref in refx:
                ref.set_data([], [])
            for ref in refy:
                ref.set_data([], [])
            # only clear trajectories when traj_clear == True
            if traj_clear == True:
                for tr in trajs:
                    tr.set_data([], [])
            # has to return a tuple of modified elements
            return (lines, joints, *refx, *refy, *trajs)

        # called each animation step, argument is incremental frame counter
        def animate(frame):
            # calculate directGeometry
            qi = [
                qi_list[frame][i] for i in range(len(self.l))
            ]
            Pi = self.directGeometry(qi)

            # add points to trajectories if True
            n = len(self.l)
            for i in range(len(traj)):
                if traj[i] == True:
                    data = trajs[i].get_data()
                    data[0].append(Pi[n-i][0])
                    data[1].append(Pi[n-i][1])
                    trajs[i].set_data(*data)

            # draw lines and joints
            lines.set_data(
                [P[0] for P in Pi],
                [P[1] for P in Pi]
            )
            joints.set_data(
                [Pi[i][0] for i in range(len(self.l))],
                [Pi[i][1] for i in range(len(self.l))]
            )
        
            # draw referential frames
            for i in range(len(refx)):
                P1 = Pi[i]
                P2 = Pi[i+1]
                x = np.subtract(P2, P1)
                x = x / np.linalg.norm(x) * l
                y = [-x[1], x[0]]
                refx[i].set_data([P1[0], P1[0] + x[0]], [P1[1], P1[1] + x[1]])
                refy[i].set_data([P1[0] + y[0], P1[0]], [P1[1] + y[1], P1[1]])

            # has to return a tuple of modified elements
            return (lines, joints, *refx, *refy, *trajs)

        # creates the animation, has to be stored in a variable!
        anim = animation.FuncAnimation(
            fig,
            animate,
            init_func    = init,
            frames       = n,
            interval     = interval,
            blit         = True
        )

        # show window and start animation
        plt.show()
