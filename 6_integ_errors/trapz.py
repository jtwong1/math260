# Example code: trapezoidal rule + error test

import numpy as np
import matplotlib.pyplot as plt


def trapz(f, a, b, n):
    """ trapezoidal rule, n sub-intervals """
    total = 0.5*(f(a) + f(b))
    h = (b-a)/n
    for k in range(1, n):
        total += f(a + k*h)
    total *= h
    return total


def func1(x):
    return np.exp(x)

def simple_test():
    """ Example: calculate the error with n, 2n sub-intervals and compare """
    a = 0
    b = 2
    exact = np.exp(b) - np.exp(a)

    n = 4
    h = (b-a)/n
    approx1 = trapz(func1, a, b, n)
    approx2 = trapz(func1, a, b, 2*n)

    err1 = np.abs(exact - approx1)
    err2 = np.abs(exact - approx2)

    print(f"exact: {exact:.6f}")
    print(f"with h={h}: est={approx1:.6f} and err={err1:.2e}")
    print(f"using h/2: est={approx2:.6f} and err={err2:.2e}")


def error_test():
    """ Example: use the exact solution to calculate error, then plot it """
    n = [2**k for k in range(3, 12)]
    exact = np.e - 1

    # compute approx. (in case its needed) and error
    approx = [trapz(func1, 0, 1, v) for v in n]
    err = [np.abs(a - exact) for a in approx]

    # plot the error (log-log)
    plt.figure(figsize=(6, 4))
    plt.loglog(n, err, '.-k', markersize=12)

    # plot a reference line
    vals = [100*v**(-2) for v in n]
    plt.loglog(n, vals, '--r')

    # plot decorations, save plot
    plt.xlabel('$n$')
    plt.ylabel('err')
    plt.savefig('trapz.pdf', bbox_inches='tight')
    plt.show()


def func2(x):  # an example function (no exact solution)
    return np.exp(3*np.sin(8*x))


def ratios_test():
    """ Example: calculate successive ratios to estimate convergence rate """
    n = [2**k for k in range(3, 12)]
    exact = np.e - 1
    approx = [trapz(func2, 0, 1, v) for v in n]
    err = [np.abs(a - exact) for a in approx]

    for k in range(len(n)):
        if k < len(n)-2:
            r = (approx[k+2] - approx[k+1]) / (approx[k+1] - approx[k])
        print("{} & {:.4f} & {:.4f}".format(n[k], approx[k], -np.log2(r)))
