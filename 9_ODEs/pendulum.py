# forced pendulum examples from class
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi, sin
import util


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


# Examples:
# forced(0, 0, damping=0.05, vel=2) (over the top)
# forced(0, 0, damping=0.1, vel=2) (not enough)
# forced(0.2, 1, damping=0, mult=25) (almost resonance)
# forced(1, 1, damping=0, mult=15) (over the top)
def forced(amp, om, damping=0, vel=0, mult=10, lines=True):
    """ Example for the forced pendulum, with
        forcing = A*sin(om*t),
        initial position/velocity pi/4 and vel
        plotted in the interval[0, mult*pi].
        lines, optionally, draws lines at 0, pi, 2*pi
    """
    h = 0.1

    def ode_func(t, x):
        return np.array([x[1], -sin(x[0]) - 2*damping*x[1] - amp*sin(om*t)])

    t, x = util.rkf(ode_func, [0, mult*pi], [pi/4, vel], hmin=h, hmax=h)
    plt.figure()
    plt.plot(t, x[:, 0], '-k')
    if lines:
        plt.plot(t, 0*t, '--r', t, 0*t + pi, '--b', t, 0*t + 2*pi, '--r')
    plt.xlabel("$t$")
    plt.show()


# Examples:
# forced_double(1) (stays close)
# forced_double(1.1) (does not stay close)
# forced_double(1.1, delta = 0.001, m=30) (still, ends up far apart)
# forced_double(1.1, delta = 0.001, m=30, euler=True)
def forced_double(amp, m=10, delta=0.01, euler=False):
    """ Sensitivity example, forced pendulum,
        x'' + 2*damping*x' + sin(x) = A*sin(omega*t)
        with two different initial conditions:
        x(0) = pi/4, x'(0) = 0 OR x(0) = pi/4 + delta, x'(0) = 0
        The sensitivy means Euler's method may give very diff. results!"""
    h = 0.02
    damping = 0.1
    om = 0.9

    def ode_func(t, x):
        return np.array([x[1], -sin(x[0]) - 2*damping*x[1] - amp*sin(om*t)])

    t, x = util.rkf(ode_func, [0, m*pi], [pi/4, 0], hmin=h, hmax=h)
    t2, x2 = util.rkf(ode_func, [0, m*pi], [pi/4 + delta, 0], hmin=h, hmax=h)
    plt.plot(t, x[:, 0], '-k', t2, x2[:, 0], '-r')
    plt.xlabel("$t$")
    plt.show()


def forced_euler():
    """ Same equation as above, comparing Euler's method to rkf """
    h = 0.02
    heuler = 0.001
    damping = 0.1
    om = 0.9
    amp = 1.1
    m = 30

    def ode_func(t, x):
        return np.array([x[1], -sin(x[0]) - 2*damping*x[1] - amp*sin(om*t)])

    plt.figure()
    t, x = fwd_euler_sys(ode_func, 0, m*pi, [pi/4, 0], heuler)
    t2, x2 = util.rkf(ode_func, [0, m*pi], [pi/4, 0], hmin=h, hmax=h)
    plt.plot(t, x[0], '-k', t2, x2[:, 0], '-r')
    plt.legend(['rkf', 'euler'])
