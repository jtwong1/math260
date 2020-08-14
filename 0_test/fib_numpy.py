"""
Small example (Fibonacci numbers)
to test python + numpy plotting
@author: jtwong
"""
import matplotlib.pyplot as plt


def fibonacci(n):
    '''Computes F_0, F_1, ...,x F_n'''
    seq = [0]*n
    seq[0] = 1
    seq[1] = 1

    for j in range(2, n):
        seq[j] = seq[j-1] + seq[j-2]

    return seq


if __name__ == '__main__':
    N = 10  # (...or set other ways...)
    fib = fibonacci(N)
    print(fib)
    print('F_{} = {}'.format(N, fib[N-1]))
    plt.plot(range(N), fib, '.k')
