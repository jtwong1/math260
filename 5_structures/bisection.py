""" bisection (recursive) version - just as an example
(not the suggested way to implement it)

Illustrates:
    - a simple use of recursion (with one call at each depth)
    - passing a parameter (# of iterations) to track some value
"""


def bisection(func, a, b, tol, it=0):
    """ bisection should take in a function f(x) """
    fa = func(a)
    fb = func(b)
    c = 0.5*(a + b)
    fc = func(c)

    if fa*fb > 0:
        raise ValueError("Bracketing failure!")

    # stop case: interval width is small or f(c) is close enough to zero
    if b - a < 2*tol or abs(fc) < 1e-24:
        return c, it

    # recursive part
    if fa*fc < 0:
        return bisection(func, a, c, tol, it+1)
    else:
        return bisection(func, c, b, tol, it+1)


def f1(x):  # one of the HW 3 examples
    return x**2 - 9


if __name__ == "__main__":
    # some bisection examples
    c, it = bisection(f1, 1, 4, 1e-6)
    print(f"found zero x={c:.8f} in {it} steps")
