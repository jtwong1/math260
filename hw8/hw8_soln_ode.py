# Partial solutions for HW 7
# (some sections omitted that are used in HW 8)

import numpy as np
import matplotlib.pyplot as plt
from numpy import pi


def rk4(func, interval, y0, h):
    """ RK4 method to solve a scalar ODE """
    y = y0
    t = interval[0]
    yvals = [y]
    tvals = [t]
    while t < interval[1] - 1e-12:
        f0 = func(t, y)
        f1 = func(t + 0.5*h, y + 0.5*h*f0)
        f2 = func(t + 0.5*h, y + 0.5*h*f1)
        f3 = func(t + h, y + h*f2)
        y += (1.0/6)*h*(f0 + 2*f1 + 2*f2 + f3)
        t += h
        yvals.append(y)
        tvals.append(t)

    return np.array(tvals), np.array(yvals)


def rk4_convergence():
    """ Convergence test for rk4, using the ODE y' = y*cos(t).
        The expected order is 4 (error = O(h^4))
    """

    def ode_func(t, y):  # a generic ODE (y'= y*cos(t)) for testing
        return y*np.cos(t)

    def sol_exact(t, y0):
        return y0*np.exp(np.sin(t))

    m = 12
    y0 = 1
    hvals = np.array([2**(-k) for k in range(m)])
    err = [0]*m
    # Version 1: using maximum error and exact solution
    for k in range(m):
        t, y_approx = rk4(ode_func, (0, 2), y0, hvals[k])
        err[k] = np.max(np.abs(sol_exact(t, y0) - y_approx))

    ref_line = 10*hvals**4
    plt.figure()
    plt.loglog(hvals, err, '.--k', hvals, ref_line, '--r')
    plt.legend(['err', 'slope 4'])
    plt.show()

    # Version 2: using the endpoint error, ratios
    y_end = [0]*m
    ratios = [0]*m
    for k in range(m):
        t, y_approx = rk4(ode_func, (0, 2), y0, hvals[k])
        y_end[k] = y_approx[-1]
        if k >= 2:
            ratios[k] = (y_end[k-1] - y_end[k-2])/(y_end[k] - y_end[k-1])
        print("h={:.2e} \t y(b)={:.6f} \t order={:.2f}"
              .format(hvals[k], y_end[k], np.log2(ratios[k])))


def orbit(interval, ic, h):
    """ solves the system x' = y, y' = -x using the trapezoidal method.
        In implicit form, the formula is
        x(n+1) = x(n) + (h/2)*(y(n+1) + y(n))
        x(n+1) = x(n) + (h/2)*(y(n+1) + y(n))
        and can be rewritten in the form
        x(n+1) = c0*x(n) + c1*y(n),
        y(n+1) = d0*x(n) + d1*y(n)
        with coefficients as defined below
    """
    det = 1 + 0.25*h**2
    c0 = (1 - 0.25*h**2)/det
    c1 = h/det
    d0 = -c1
    d1 = c0

    t = interval[0]
    x, y = ic
    tvals = [t]
    sol = [(x, y)]  # (opposite of data format used in class)
    while t < interval[1] - 1e-12:
        tmp = c0*x + c1*y
        y = d0*x + d1*y
        x = tmp
        t += h
        tvals.append(t)
        sol.append((x, y))
    return tvals, sol


# the key feature illustrated here is that the trapezoidal method
# produces closed orbits (even for the approximation!) for any h.
# In fact, it conserves a `discrete' energy E_h = E + O(h)
# where E is the true energy x^2 + y^2 conserved by the true solutionn.
# This conservation ensures that orbits stay closed (almost circles)
def circle_example(h):
    """ circular motion example, solving
        x' = y,  y' = -x
        with solutions x(t) = A*cos t, y(t) = A*sin(t)
        (note: in code, v is the vector (x,y))
    """
    ic = (1.0, 0)
    interval = (0, 100)  # many periods - still almost a circle!

    t, sol = orbit(interval, ic, h)
    x, y = ([s[dim] for s in sol] for dim in (0, 1))

    # phase plane plot
    plt.figure()
    t = np.linspace(0, 2*pi, 100)
    plt.plot(x, y, '-k', np.cos(t), np.sin(t), '--b')
    plt.legend(["approx.", "exact"])
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.axis('equal')
    plt.show()
