"""
Math 260, Fall 2020
Example: demo of debugging with fibonacci numbers
"""


def fib_list(n):
    """ Computes a list of Fibonacci numbers """
    fibs = [0]*n
    fibs[0] = 1
    fibs[1] = 1

    for k in range(2, n):
        # ... add output here? ...
        print(k, fibs[k])
        fibs[k] = fibs[k-1] + 2*fibs[k-2]

    return fibs


if __name__ == '__main__':
    n = 15
    f = fib_list(n)
    print(f)
    print('F_{} = {}'.format(n, f[n-1]))
