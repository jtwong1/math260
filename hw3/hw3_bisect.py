""" HW 3: example solutions: bisection
Note that you can choose whatever type of error you want, as long
as it makes sense.
"""
import numpy as np


def find_zero(func, a, b, tol=1e-6, show=False, ftol=1e-20):
    """ bisection should take in a function f(x) """
    fa = func(a)
    fb = func(b)

    if fa*fb > 0:
        raise ValueError(f"Endpoints {a}, {b} do not bracket... "
                         + f"(f-values: {fa:.4f}, {fb:.4f}.)")

    it = 0
    if tol > (b-a)/2:
        return 0.5*(b+a), 0  # trivial case

    if show:
        print("iter. \t midpoint")
    while b-a > 2*tol:
        c = 0.5*(a + b)
        fc = func(c)
        if show:
            print(f"it {it}: {c:.8f}")

        if abs(fc) < ftol:  # special case: f(c) is close enough to zero
            return c, it

        if fa*fc < 0:
            b = c
        else:
            a = c
            fa = fc

        it += 1

    return c, it


def f1(x):  # one of the HW 3 examples
    return x**2 - 9


# For Q2c: Note that machine precision is ~2^(-52),
# so we can't expect to get better than about this accuracy (~1e-16).
# Thus, for an interval of size ~1, about 50 steps is the largest
# reasonable amount.
#
# After this point, you may just get b - a = 0 exactly, which ends the loop.
# Depending on how it is written, you could end up with an infinite loop,
# e.g. if you track the difference b - a directly instead of a and b.

if __name__ == "__main__":
    # some bisection examples
    c, it = find_zero(f1, 1, 4, tol=1e-6, show=True)
    c, it = find_zero(np.sin, 1, 4, tol=1e-6, show=False)
    print(f"\nsin(x): found zero x={c:.8f} in {it} steps")

    c, it = find_zero(f1, 1, 4, tol=1e-21, show=True)

    # testing the error code
    # c = find_zero(np.sin, 0.2, 0.7, tol=1e-6, show=True)
