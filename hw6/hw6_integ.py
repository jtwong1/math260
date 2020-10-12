""" HW 6 solution code: !Q1 and Q2"""
import numpy as np
import matplotlib.pyplot as plt


MAX_DEPTH = 10


def simp(fun, a, b):
    """ simpson's rule, two sub-intervals for integ """
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


def simpson(func, a, b, n):
    """ simpson's rule, n sub-intervals (equally spaced) """
    if n % 2 == 1:
        raise ValueError("n must be even!")
    h = (b-a)/n
    total = func(a)
    for k in range(1, n//2+1):
        mid = a + (2*k-1)*h
        total += 4*func(mid)
        total += 2*func(mid + h)
    return (total - func(b))*h/3


def trapz(f, a, b, n):
    total = 0.5*(f(a) + f(b))
    h = (b-a)/n
    for k in range(1, n):
        total += f(a + k*h)
    total *= h
    return total


# functions used for the questions...
def func1a(x):
    return (1-x**2)**2


def func1b(x):
    return np.exp(np.sin(2*x)**2)


def func1c(x):
    return 1/(4*np.sin(2*x)**2 + 1)


def q1a_test():
    """ test for Q1a: Simpson's rule, convergence rate (2nd order) """

    # compute approximations, errors
    nvals = [2**k for k in range(3, 12)]
    exact = 46/15
    integrals = [simpson(func1a, 0, 2, n) for n in nvals]
    err = [np.abs(approx - exact) for approx in integrals]

    # create reference line
    slope = -4
    ref_line = [100*n**slope for n in nvals]

    plt.figure(figsize=(4, 3.5))
    plt.loglog(nvals, err, '.-k', nvals, ref_line, '--r', markersize=12)
    plt.xlabel('$n$')
    plt.ylabel('err')
    plt.legend(['error', f'slope {slope}'])
    plt.savefig('trapz.pdf', bbox_inches='tight')
    plt.show()


def q1b_test():
    """ test for Q1b: Simpson's rule convergence rate (linear) """

    nvals = np.array(range(4, 200, 2))
    exact = 1.404962946208145
    integrals = [simpson(func1c, 0, np.pi, n) for n in nvals]
    err = [np.abs(approx - exact) for approx in integrals]

    rate = 0.8  # ref line slope (from eyeballing the data)
    rate = np.exp(-0.5*np.arcsinh(0.5))  # exact rate (from theory)
    ref_line = [100*rate**n for n in nvals]

    plt.figure(figsize=(4, 3.5))
    plt.semilogy(nvals, err, '.-k', nvals, ref_line, '--r', markersize=12)
    plt.xlabel('$n$')
    plt.ylabel('err')
    plt.legend(['error', f'ref line, r={rate:.2f}'])
    plt.savefig('trapz.pdf', bbox_inches='tight')
    plt.show()


def func2a(x):
    return 5*np.exp(-50*x) + np.sin(x)


def q2a_test():
    exact = 1/10*(21 - np.exp(-50*np.pi))
    a = 0
    b = np.pi
    tol = 1e-4

    approx, left = integrate(func2a, a, b, tol)
    err = abs(approx - exact)

    # get equally spaced approx. with the same err. bound
    err_s = 1
    n_equal = 2
    while err_s > tol:
        n_equal *= 2
        s = simpson(func2a, a, b, n_equal)
        err_s = abs(s - exact)

    print('Adapt: err = {:.2e}, {} intervals'.format(err, len(left)))
    print('Equal: err = {:.2e}, {} intervals'.format(err_s, n_equal))
