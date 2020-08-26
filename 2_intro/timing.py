"""
Math 260, Fall 2020
Timing examples from the lecture:
    - pre-allocation of arrays
    - row vs. col major ordering for matrices
"""
import time


def timer(name, func, *args):
    """ quick code to time execution of a function.
        Note that python provides a built-in for this
        in the timeit module (timeit.timeit).
    """
    start = time.perf_counter()  # start timer
    result = func(*args)
    elapsed = time.perf_counter() - start  # end timer
    print("time ({}): {:.3f} msec".format(name, elapsed*1000))
    return elapsed, result


def array_pre(n):
    """ build an array: pre-allocate"""
    x = [0]*n
    for k in range(n):
        x[k] = k
    return x


def array_app(n):
    """ build an array: append one at a time """
    x = []
    for k in range(n):
        x.append(k)


def array_test(n):
    """ Compare pre-allocation to append """
    timer("pre", array_pre, n)
    timer("app", array_app, n)


def mat_rowmaj(mat):
    """ Sum elements of a matrix, *row-major* (jk) order """
    n = len(mat)
    total = 0
    for j in range(n):
        for k in range(n):
            total += mat[j][k]
    return total


def mat_colmaj(mat):
    """ Sum elements of a matrix, *col-major* (kj) order """
    n = len(mat)
    total = 0
    for k in range(n):
        for j in range(n):
            total += mat[j][k]
    return total


def mat_test(n):
    """ Compare row and col. major ordering
        for sum of elements in a matrix.
    """
    mat = [None]*n
    for k in range(n):
        mat[k] = [1/(k+1) for k in range(n)]

    timer("row maj. (jk)", mat_rowmaj, mat)
    timer("col maj. (kj)", mat_colmaj, mat)
