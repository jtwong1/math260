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


def integrate(func, a, b, tol=1e-8):
    """ Integrates a function from a to be using an adaptive scheme.
        Args:
            func - the function f(x) to integrate
            a, b - the interval of integration
            tol - error tolerance (solution estimates abs. error < tol)
        Returns:
            integral - the approximation
            left_pts - list of the left endpts of intervals used (for testing)
    """
    left_pts = []
    result = integ(func, a, b, tol, 0, left_pts)

    return result, left_pts


def integ(fun, a, b, tol, depth, endpt):
    """ recursive adaptive scheme. Tracks left endpoint of sub-intervals
        used in the shared list `endpt' for testing."""
    c = 0.5*(a+b)
    approx1 = simp(fun, a, b)
    approx2 = simp(fun, a, c) + simp(fun, c, b)

    err_approx = (16/15)*abs(approx1 - approx2)

    if err_approx < tol or depth > MAX_DEPTH:
        endpt.append(a)
        return approx2

    integ_left = integ(fun, a, c, tol/2, depth+1, endpt)
    integ_right = integ(fun, c, b, tol/2, depth+1, endpt)
    return integ_left + integ_right


def integrate_stack(fun, a, b, tol=1e-8):
    """ adaptive scheme [with a stack].
        Tracks sub-intervals used for testing."""
    stack = [(a, b)]
    tol = tol/(b-a)  # fix tolerance (so err < tol*(b-a))
    total = 0
    min_size = (b-a)/2**(MAX_DEPTH)
    intervals = []
    while stack:
        a, b = stack.pop()
        mid = 0.5*(a + b)
        a1 = simp(fun, a, b)
        a2 = simp(fun, a, mid) + simp(fun, mid, b)
        err_approx = (16/15)*abs(a1 - a2)

        if b-a <= min_size or err_approx < tol*(b-a):
            total += a1
            intervals.append((a, b))
        else:
            stack.extend([(a, mid), (mid, b)])

    return total, intervals


def f(x):
    return np.sin(1.0/x)


if __name__ == '__main__':
    exact = 0.51301273999140998  # from wolfram alpha
    a = 0.1
    b = 1
    tol = 2e-5

    approx, left = integrate(f, a, b, tol)
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
