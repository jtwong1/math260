# template code for HW 10
# Given (to be used directly):
# - rk4 method for solving a system of ODEs
# - function to load SIR data for fitting
# Examples (not used directly):
# - solving an ODE system with rk4 (with some parameters)

import matplotlib.pyplot as plt
import numpy as np


def rk4(func, interval, y0, h):
    """ RK4 method, to solve the system y' = f(t,y) of m equations
        Inputs:
            f - a function returning an np.array of length m
         a, b - the interval to integrate over
           y0 - initial condition (a list or np.array), length m
           h  - step size to use
        Returns:
            t - a list of the times for the computed solution
            y - computed solution; list of m components (len(y[k]) == len(t))
    """
    y = np.array(y0)
    t = interval[0]
    tvals = [t]
    yvals = [[v] for v in y]  # y[j][k] is j-th component of solution at t[k]
    while t < interval[1] - 1e-12:
        f0 = func(t, y)
        f1 = func(t + 0.5*h, y + 0.5*h*f0)
        f2 = func(t + 0.5*h, y + 0.5*h*f1)
        f3 = func(t + h, y + h*f2)
        y += (1.0/6)*h*(f0 + 2*f1 + 2*f2 + f3)
        t += h
        for k in range(len(y)):
            yvals[k].append(y[k])
        tvals.append(t)

    return tvals, yvals


def read_sir_data(fname):
    """ Reads the SIR data for the HW problem.
        Inputs:
            fname - the filename (should be "sir_data.txt")
        Returns:
            t, x - the data (t[k], I[k]), where t=times, I= # infected
            pop - the initial susceptible population (S(0))
    """
    with open(fname, 'r') as fp:
        parts = fp.readline().split()
        pop = float(parts[0])
        npts = int(float(parts[1]))
        t = np.zeros(npts)
        x = np.zeros(npts)

        for k in range(npts):
            parts = fp.readline().split()
            t[k] = float(parts[0])
            x[k] = float(parts[1])

    return t, x, pop


def example_odef(t, x, params):
    """ example ODE (not the SIR one),
        u' = a*u + v
        v' = u + b*v
    """
    du = params[0]*x[0] + x[1]
    dv = x[0] + params[1]*x[1]
    return np.array((du, dv))


if __name__ == '__main__':

    # load data; plot
    tvals, data, pop = read_sir_data('sir_data.txt')
    plt.figure(1)
    plt.plot(tvals, data, '.k', markersize=12)
    plt.show()

    # example ODE solve after picking some parameters
    a = -1
    b = -2
    x0 = np.array((1.0, 0.0))
    h = 0.1
    t, x = rk4(lambda t, x: example_odef(t, x, (a, b)),
               (0, 10), x0, h)

    plt.figure(2)
    plt.plot(t, x[0], '-k', t, x[1], '-r')
    plt.xlabel('t')
    plt.legend(['u(t)', 'v(t)'])
    plt.show()
