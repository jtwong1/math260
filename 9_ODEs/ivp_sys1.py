# Lecture examples for systems of ODEs:
#   - Euler's method for systems
#   - damped (linear) pendulum
#   - simple harmonic motion (phase plane plot)

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi


def fwd_euler_sys(f, a, b, y0, h):
    """ Forward euler, to solve the system y' = f(t,y) of m equations
        Inputs:
            f - a function returning an np.array of length m
         a, b - the interval to integrate over
           y0 - initial condition (a list or np.array), length m
           h  - step size to use
        Returns:
            t - a list of the times for the computed solution
            y - computed solution; list of m components (len(y[k]) == len(t))
    """
    y = np.array(y0)  # copy!
    t = a
    tvals = [t]
    yvals = [[v] for v in y]  # y[j][k] is j-th component of solution at t[k]
    while t < b - 1e-12:
        y += h*f(t, y)
        t += h
        for k in range(len(y)):
            yvals[k].append(y[k])
        tvals.append(t)

    return tvals, yvals


def system_example(h, damping=0.2, end_time=6*pi):
    """ damped pendulum (linear) example, to solve
        x'' + damping*x' + x = 0"""

    def ode_func(t, x):
        return np.array([x[1], -x[0] - 2*damping*x[1]])

    x_init = [pi/4, 0]
    t, x = fwd_euler_sys(ode_func, 0, end_time, x_init, h)

    plt.figure()
    plt.plot(t, x[0], '-k', t, x[1], '-r')
    plt.legend(["$\\theta(t)$", "$\\theta'(t)$"])
    plt.xlabel("$t$")
    plt.title(f"damping={damping:.1f}")
    plt.show()


def circle_example(h, periods=2):
    """ circular motion example, solving
        x' = y,  y' = -x
        with solutions x(t) = A*cos t, y(t) = A*sin(t)
        (note: in code, v is the vector (x,y))
    """

    def ode_func(t, v):
        return np.array([v[1], -v[0]])

    v_init = [1.0, 0]
    t, v = fwd_euler_sys(ode_func, 0, periods*2*pi, v_init, h)
    x = v[0]
    y = v[1]

    # plot vs. t
    plt.figure()
    plt.plot(t, x, '-k', t, y, '-r')
    plt.legend(["$\\theta(t)$", "$\\theta'(t)$"])
    plt.xlabel("$t$")
    plt.show()

    # phase plane plot
    plt.figure()
    t = np.linspace(0, 2*pi, 100)
    plt.plot(x, y, '-k', np.cos(t), np.sin(t), '--b')
    plt.legend(["approx.", "exact"])
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()
