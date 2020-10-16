# Code to make class example run: 
# - ref line drawing function for convenience
# - rkf method (adaptive RK method)
# (note that you could also use scipy's ode integrate
#	function, which uses a similar method)

import numpy as np
import matplotlib.pyplot as plt


def refline(x, y, slope, offset, side=0):
    """ computes a ref line next to data y = Cx^p with
     estimated p = slope, offset by 'offset' decades,
      on the left (side=0) or right (side=1)."""
    if side == 0:
        base = 0
        ind0 = 0
        ind1 = len(x) // 2
    else:
        base = len(x) - 1
        ind0 = len(x) // 2
        ind1 = len(x)

    y = [10 ** offset * y[base] * (v / x[base]) ** slope for v in x[ind0:ind1]]
    return x[ind0:ind1], y


def rkf(func, interval, y0, hmin=1e-6, hmax=1, atol=1e-4, rtol=1e-4):

    coeffs = [[0] * 6 for i in range(6)]  # could be defined in a global

    # For coeffs[j]:
    # First entry: c_j, then a_{j,1} through a_{j,j-1}
    coeffs[1][0:2] = [1 / 4, 1 / 4]  # f2
    coeffs[2][0:3] = [3 / 8, 3 / 32, 9 / 32]  # f3
    coeffs[3][0:4] = [12 / 13, 1932 / 2197, -7200 / 2197, 7296 / 2197]
    coeffs[4][0:5] = [1, 439 / 216, -8, 3680 / 513, -845 / 4104]
    coeffs[5][0:6] = [1 / 2, -8 / 27, 2, -3544 / 2565, 1859 / 4104, -11 / 40]

    # weights for f1, f2, ... f6
    w4 = [25 / 216, 0, 1408 / 2565, 2197 / 4104, -1 / 5, 0]
    w5 = [16 / 135, 0, 6656 / 12825, 28561 / 56430, -9 / 50, 2 / 55]

    T = [interval[0]]
    u = np.array(y0)
    Y = [list(y0)]
    t = interval[0]
    it = 0
    fvals = [np.zeros(6)] * 6
    utmp = np.zeros_like(u)
    h = hmin  # start with the minimum h
    safety = 0.8

    while t < interval[1] - 1e-12:
        fvals[0] = func(t, u)
        for k in range(1, 6):
            utmp[:] = u[:]
            for m in range(1, k + 1):
                utmp += h * coeffs[k][m] * fvals[m - 1]
            fvals[k] = func(t + h * coeffs[k][0], utmp)

        utmp[:] = u[:]
        for k in range(6):
            utmp += h * w5[k] * fvals[k]
            u += h * w4[k] * fvals[k]

        t += h
        it += 1
        Y.append(list(u))
        T.append(t)

        # error estimation
        err = max(abs(u - utmp))
        if err > 0:
            h = safety * h * (min(atol, rtol * max(abs(u))) / err) ** (1 / 5)
            h = max(h, hmin)
            h = min(h, hmax)

    return np.array(T), np.array(Y)
