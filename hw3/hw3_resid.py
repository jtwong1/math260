""" HW 3: example solutions: residual calculation. You should find that
the residual is about the size of machine epsilon (as good as you can expect)
but the error is about 1e-10, which is 6 orders of magnitude larger.

The issue is that the system Hx = b is *very* sensitive (ill-conditioned)
so rounding errors propagate and become quite large. This matrix (the "Hilbert matrix")
is a well-known ill-conditioned matrix that causes trouble.

In fact, for n times n hilbert matrices (hilb), this amplification factor
grows exponentially with n - so that once n is about 15, the error renders
the solution completely unusable!
"""

import numpy as np


def residual(a, x, b):
    """ Calculates the residual A*x - b, returning a new list """
    n = len(b)
    res = [0]*n
    for k in range(n):
        res[k] = -b[k]
        for j in range(n):
            res[k] += a[k][j]*x[j]

    return res


def error_example():
    """ Solves Hx = b using Gaussian elim (with numpy's implementation),
        for a problem where the exact solution is also given.
    """
    # create the matrix and RHS for Hx = b
    n = 6
    hilb = [[1/(j + k + 1) for k in range(n)] for j in range(n)]
    b = [6, 617/140, 499/140, 2531/840, 1649/630, 12847/5544]

    x_comp = np.linalg.solve(hilb, b).tolist()  # computed solution
    x_true = [1, 2, 3, 4, 5, 6]  # true solution

    r = residual(hilb, x_comp, b)

    max_err = norm([x - y for x, y in zip(x_comp, x_true)])
    max_res = norm(r)

    print(f"Largest component of error: {max_err:.2e}")
    print(f"Largest component of resid: {max_res:.2e}")


def norm(x):
    """ Max norm for a vector x (max. abs value of a component) """
    return max([abs(v) for v in x])
