"""Lecture example: adaptive integration using Simpson's rule.
Two versions: recursive, and using a stack instead.
"""

import numpy as np
import matplotlib.pyplot as plt


MAX_DEPTH = 10  # max recursion depth


def simp(fun, a, b):
    """ simpson's rule, two sub-intervals for integ routine """
    h = 0.5*(b-a)
    c = 0.5*(a+b)
    return (h/3)*(fun(a) + 4*fun(c) + fun(b))


def integ(fun, a, b, tol=1e-8, depth=0, endpt=[]):
    """ recursive adaptive scheme. Tracks left endpoint of sub-intervals
        used in the shared list `endpt' for testing."""
    c = 0.5*(a+b)
    a1 = simp(fun, a, b)
    a2 = simp(fun, a, c) + simp(fun, c, b)

    err = (16/15)*abs(a1 - a2)

    if err < tol or depth > MAX_DEPTH:
        endpt.append(a)
        return a1, endpt

    a1 = integ(fun, a, c, tol/2, depth+1)[0]
    a2 = integ(fun, c, b, tol/2, depth+1)[0]
    return a1 + a2, endpt


def integ_stack(fun, a, b, tol=1e-8):
    """ adaptive scheme [with a stack].
        Tracks sub-intervals used in subs for testing."""
    stack = [(a, b)]
    tol = tol/(b-a)  # fix tolerance (so err < tol*(b-a))
    total = 0
    min_size = (b-a)/2**(MAX_DEPTH)
    subs = []
    while stack:
        a, b = stack.pop()
        c = 0.5*(a + b)
        a1 = simp(fun, a, b)
        a2 = simp(fun, a, c) + simp(fun, c, b)
        err = (16/15)*abs(a1 - a2)

        if b-a <= min_size or err < tol*(b-a):
            total += a1
            subs.append((a, b))
        else:
            stack.extend([(a, c), (c, b)])

    return total, subs


def f(x):
    return np.sin(1.0/x)


if __name__ == '__main__':
    exact = 0.51301273999140998  # from wolfram alpha
    a = 0.1
    b = 1
    tol = 2e-5

    approx, left = integ(f, a, b, tol)
    err = abs(approx - exact)

    print(f"Adapt: err = {err:.2e}, {len(left)} intervals")

    # plotting to show the mesh of points for the adaptive method.
    x = np.linspace(a, b, 100)
    left = np.array(left)  # convert to numpy arrray for vectorized math

    plt.figure(figsize=(3, 2.5))
    plt.plot(left, f(left), '.b')  # plot left sub-interval points
    plt.plot(x, f(x), '--k')
    plt.xlabel('$x$')
    plt.show()
