"""
Short derivative example - rounding error for a forward difference
-> Version 1: prints a table of the error
-> Version 2: makes a log-log plot (more on this later)
"""
import numpy as np
import matplotlib.pyplot as plt


def deriv(f, x, h):
    """ simple forward difference approx. for f'(x) """
    return (f(x+h) - f(x))/h


def err_table(n):
    """ table of errors for 10^(-1), ... 10^(-n) """
    h = 1
    x0 = 1
    exact = np.cos(x0)
    for k in range(n):
        h /= 10
        err = abs(deriv(np.sin, x0, h) - exact)
        print(f'{h:.1e} \t {err:.1e}')


def err_plot():
    """ log-log plot of error vs. h for the forward difference"""

    # choose a good density of points, all log-spaced
    hvals = [4**(-k) for k in range(26) if 4**(-k) > 1e-16]
    x0 = 1
    exact = np.cos(x0)
    err = [np.abs(deriv(np.sin, x0, h) - exact) for h in hvals]

    # plot using pyplot: with and without reference line
    for j in range(2):
        plt.figure()
        plt.loglog(hvals, err, '.-k', markersize=12)
        if j == 0:  # for comparison (slope 1 on plot), add this to a 2nd ver.
            plt.loglog(hvals, hvals, '--r')
            plt.legend(['err', 'C*h'])
        plt.xlabel('h')
        plt.ylabel('err')
        plt.ylim([1e-12, 1])
        plt.show()
