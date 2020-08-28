"""
Math 260, Fall 2020
Timing exercise: example solution
"""

import time


# ---------------------------------------------------
def hilb(n):
    return [[1/(j+k+1) for k in range(n)] for j in range(n)]


def hilb_for(n):
    """ Note that this is a messy solution;
    the list comprehension version is preferred
    for practical use."""

    mat = [None]*n  # create a list of n somethings
    # (note that these will be overwritten, so it
    # does not matter what they are, e.g. mat = ['??']*n)
    for j in range(n):
        mat[j] = [0]*n  # set k-th element to a list of n 0's
        for k in range(n):
            mat[j][k] = 1/(j+k+1)

    return mat


def sum_by_row(mat):
    """ assumes mat is a square matrix """
    total = 0
    n = len(mat)
    for j in range(n):
        for k in range(n):
            total += mat[j][k]
    return total


def sum_by_col(mat):
    # (sum the matrix entries)
    total = 0
    n = len(mat)
    for k in range(n):
        for j in range(n):
            total += mat[j][k]


if __name__ == "__main__":
    # create the hilbert matrix, then sum it by rows / by cols and compare time

    n = 2000
    mat = hilb(n)

    start = time.perf_counter()
    # ... sum by rows ...
    total = sum_by_row(mat)
    elapsed1 = time.perf_counter() - start

    start = time.perf_counter()
    # ... sum by columns ...
    total = sum_by_col(mat)
    elapsed2 = time.perf_counter() - start

    print("Sum by rows: {:.3f} s".format(elapsed1))
    print("Sum by cols: {:.3f} s".format(elapsed2))
