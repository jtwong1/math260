"""
Math 260, Fall 2020
Timing exercise
"""
import time


def example():
    """ Related example code: measure time to find the
        maximum element of a list..."""
    # create a list
    n = 10000
    x = [0]*n
    for k in range(n):
        x[k] = k

    # test timing for finding max.
    start = time.perf_counter()  # gets `current time'
    largest = x[0]
    for k in range(1, n):
        largest = max(largest, x[k])

    elapsed = time.perf_counter() - start  # end timer
    print("time: {:.3f} sec".format(elapsed))


# ---------------------------------------------------
def hilb(n):
    return [[1/(j+k+1) for k in range(n)] for j in range(n)]


def hilb_for(n):
    """ list comprehension review """
    # as hilb, but with for loops
    ...
    return ...


def sum_by_row(mat):
    total = 0
    n = len(mat)
    # (sum the matrix entries)
    ...
    return total


def sum_by_col(mat):
    # (sum the matrix entries)
    ...


if __name__ == "__main__":
    # create the hilbert matrix, then sum it by rows / by cols and compare time

    n = 2
    mat = hilb(n)

    start = time.perf_counter()
    # ... sum by rows ...
    ...
    elapsed = time.perf_counter() - start

    start = time.perf_counter()
    # ... sum by columns ...
    ...
    elapsed = time.perf_counter() - start
