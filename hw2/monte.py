"""
Math 260, Fall 2020
Homework 2 example solution:
Monte Carlo integration

See notes above main for a brief discussion.
"""

import random
import numpy as np
import matplotlib.pyplot as plt


def monte(f, box, n, trials):
    """ Estimates int_a^b f(x) dif x using Monte Carlo integration.
        Assumes f(x) is positive for all x.
        Args:
            f - the function to integrate
            box - a tuple (a, b, height) for the bounding rectangle
            n - number of sample points
            trials - repeat this many times
    """

    est = 0
    box_area = (box[1] - box[0])*box[2]
    for k in range(trials):
        count = 0
        for j in range(n):
            x = random.uniform(box[0], box[1])
            y = random.uniform(0, box[2])

            if y < f(x):
                count += 1

        est += (count/n)*box_area

    return est/trials


def arc(x):
    return np.sqrt(1-x**2)


# Notes:
# Create a table of errors vs. n
# Note that the expected error goes like ~C/sqrt(n) (from probability)
# so the convergence is *very* slow.
# about ~ n=10000 is needed (maybe a bit less) needed to get 3.14 reliably.
#
# One needs to do alot more calculation to see the expected error behavior.
if __name__ == "__main__":
    trials = 100
    nvals = [1000*k for k in range(1, 11)]

    n = len(nvals)
    approx = [0]*n
    err = [0]*n

    for k in range(n):
        approx[k] = 4*monte(arc, (0, 1, 1), nvals[k], trials)
        err[k] = abs(approx[k] - np.pi)

    for k in range(n):
        print("{} \t {:.5f} \t {:.5f}".format(nvals[k], approx[k], err[k]))

    plt.loglog(nvals, err)
