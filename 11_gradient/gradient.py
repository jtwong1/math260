# Example of gradient descent on a simple function
# includes some extra output to track the points taken
# and plots the path on a contour plot

import matplotlib.pyplot as plt
import numpy as np


def minimize(f, df, x0, tol=1e-4, maxsteps=100, verb=False):
    """ Gradient descent with a *very simple* line search
        Inputs:
            f - the function f(x)
            df - gradient of f(x)
            x0 - initial point
    """
    x = np.array(x0)
    err = 100
    it = 0
    pts = [np.array(x)]
    while it < maxsteps and err > tol:
        fx = f(x)
        v = df(x)
        v /= sum(np.abs(v))
        alpha = 1
        while alpha > 1e-10 and f(x - alpha*v) >= fx:
            alpha /= 2
        if verb:
            print(f"it={it}, x[0]={x[0]:.8f}, f={fx:.8f}")
        x -= alpha*v
        pts.append(np.array(x))
        err = max(np.abs(alpha*v))
        it += 1

    return x, it, pts


def func(x):
    return (x[0] - 1)**2 + 4*x[1]**2


def dfunc(x):  # gradient of func
    dx = 2*(x[0] - 1)
    dy = 8*(x[1])
    return np.array((dx, dy))


if __name__ == '__main__':

    # gradient descent example
    min_true = np.array((1.0, 0))
    x0 = np.array((3.7, 1.6))
    x, it, pts = minimize(func, dfunc, x0, tol=1e-3, verb=True)

    # print of approximation + error
    np.set_printoptions(precision=4)
    print('actual: ' + str(min_true))
    print('approx: ' + str(x) + ', it={}'.format(it))
    print('error: {:.2e}'.format(max(np.abs(min_true - x))))

    # plotting the contours + path of descent
    npts = 200
    x = np.linspace(0, 4.5, npts)
    y = np.linspace(-1.5, 2, npts)
    xx, yy = np.meshgrid(x, y)
    zz = func((xx, yy))

    plt.figure()
    plt.contour(xx, yy, zz)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.plot([p[0] for p in pts], [p[1] for p in pts], '.-k', markersize=12)
    plt.show()
