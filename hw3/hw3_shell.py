""" shell for HW 3 problems.
    Note that you should replace my palceholder
    doc-strings with actual descriptive ones.
"""
import numpy as np


# ----------------------------------
# ---- Code for Q1a, Q1b, Q1c ------
# ----------------------------------

def back_solve(a, b):
    """ backward substitution, returning a new list """
    n = len(b)
    x = [0]*n
    ...
    return x


def residual(a, x, b):
    """ Calculates the residual A*x - b, returning a new list """
    n = len(b)
    res = [0]*n
    for k in range(n):
        # ... set res[k]
        ...

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

    # calculate the error between x_comp and x_exact...
    ...

    # calculate the residual for x_comp...
    ...

    # compare the max. absolute value of components for each
    # (so you should end up comparing *two numbers*)
    ...


# ------------------------------
# --------- Code for Q2 --------
# ------------------------------

def find_zero(func, a, b, tol):
    """ bisection should take in a function f(x) """
    fa = func(a)
    fb = func(b)
    # Note: it's useful to store the f(x) evaluations
    # if you use them more than once, to avoid extra work.
    # you should minimize the # of f(x) evaluations used

    # ... check that the initial interval brackets ...
    ...

    # ... the go through the bisection process ...
    it = 0
    while False:
        c = 0.5*(a + b)

    return c, it


def f1(x):  # one of the HW 3 examples
    return x**2 - 9


if __name__ == "__main__":
    # example of the tests you should run
    c = find_zero(f1, 1, 4, 1e-6)
    # c = find_zero(np.sin, 3, 4, 1e-6)

    c = 1000*np.pi
    print(f"A floating point number: {c:.6f}, and in sci. notation: {c:.2e}")
