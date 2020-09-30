# Example code: trapezoidal rule + error test

import numpy as np
import matplotlib.pyplot as plt


def trapz(f, a, b, n):
    total = 0.5*(f(a) + f(b))
    h = (b-a)/n
    for k in range(1, n):
        total += f(a + k*h)
    total *= h
    return total


def func(x):  # an example function
    return np.exp(3*np.sin(8*x))


def simple_test():
    f = lambda x: np.exp(x)
    a = 0
    b = 2
    exact = np.exp(b) - np.exp(a)

    n = 4
    h = (b-a)/n
    approx1 = trapz(f, a, b, n)
    approx2 = trapz(f, a, b, 2*n)

    err1 = np.abs(exact - approx1)
    err2 = np.abs(exact - approx2)

    print(f"exact: {exact:.6f}")
    print(f"with h={h}: est={approx1:.6f} and err={err1:.2e}")
    print(f"using h/2: est={approx2:.6f} and err={err2:.2e}")

# tests the integral of func over [0,1]
if __name__ == '__main__':
    n = [2**k for k in range(3, 12)]
    exact = np.e - 1
    approx = [trapz(func, 0, 1, v) for v in n]
    err = [a - exact for a in approx]

    for k in range(len(n)):
        if k < len(n)-2:
            r = (approx[k+2] - approx[k+1]) / (approx[k+1] - approx[k])
        print("{} & {:.4f} & {:.4f}".format(n[k], approx[k], -np.log2(r)))

    plt.figure(figsize=(3, 2.5))
    plt.loglog(n, err, '.-k', markersize=12)
    plt.xlabel('$n$')
    plt.ylabel('err')
    plt.savefig('trapz.pdf', bbox_inches='tight')
    plt.show()
