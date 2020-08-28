"""
Short derivative example - rounding error for a forward difference
-> Version 1: prints a table of the error
-> Version 2: makes a log-log plot (more on this lataer)
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
    hvals = [2**(-k) for k in range(52)]
    x0 = 1
    exact = np.cos(x0)
    err = [np.abs(deriv(np.sin, x0, h)-exact) for h in hvals]

    plt.loglog(hvals, err)
    plt.xlabel('h')
    plt.ylabel('err')
    plt.show()
