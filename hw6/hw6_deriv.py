""" HW 6 solution code: Q3"""
import numpy as np
import matplotlib.pyplot as plt


MAX_DEPTH = 10


def deriv(func, x, h):
    result = 0.5*func(x + 2*h) - func(x + h) + func(x - h) - 0.5*func(x - 2*h)
    return result/h**3


def func(x):
    return np.cos(2*x)


def d3func(x):
    return 8*np.sin(2*x)


def q3_test():
    """ test for Q3: derivative approximation """

    # compute approximations, errors
    hvals = [2**(-k) for k in range(3, 52)]
    x0 = 1
    exact = d3func(x0)

    derivs = [deriv(func, x0, h) for h in hvals]
    err = [np.abs(approx - exact) for approx in derivs]

    # create reference line
    hvals_cut = [h for h in hvals if h > 1e-8]
    ref_line = [100*h**2 for h in hvals_cut]
    ref_line2 = [1e-15*h**(-3) for h in hvals_cut]

    plt.figure(figsize=(4, 3.5))
    plt.loglog(hvals_cut, err[:len(hvals_cut)], '.-k',
               hvals_cut, ref_line, '--r',
               hvals_cut, ref_line2, '--b', markersize=12)
    plt.xlabel('$h$')
    plt.ylabel('err')
    plt.legend(['error', 'slope 2', 'slope -3'])
    plt.savefig('deriv1.pdf', bbox_inches='tight')
    plt.show()

    k = np.argmin(err)
    print("hval of smallest err: {:.2e}, with err={:.2e}"
          .format(hvals[k], err[k]))
