""" HW5:  mergseort solutions code."""
import random
import time


# the internal .sort() algorithm is optimized and quite fast
# For n=10000 I get 0.04s for mergesort
# For n=20000 I get 0.088s for mergesort
# The times are consistent with the O(n log n) scaling;
# doubling n will double the time (with a little bit more from the log (n))
#
# Note that the same holds for .sort(),
# with n=10000, 20000 I get .00132 and 0.003 seconds.

def timer(sort_method, n, trials):
    """ tests execution time for sort_method on a test array of length n """
    elapsed = 0
    for k in range(trials):
        arr = test_list(n, maxval=1000, seed=260)
        start = time.perf_counter()
        sort_method(arr)
        elapsed += time.perf_counter() - start
    return elapsed/trials


def test_list(n, maxval=1000, seed=260):
    """ list of random integers for testing sort """
    random.seed(seed)
    return [random.randint(0, maxval) for k in range(n)]


def merge_test():
    """ HW solution: correctness + timing tests for mergesort """
    arr = test_list(50, maxval=1000, seed=260)
    arr2 = arr[:]

    mergesort(arr)
    arr2.sort()

    if(arr == arr2):
        print("mergesort and .sort() agree!")

    trials = 20
    n = 10000
    time_merge = timer(mergesort, n, trials)
    time_py = timer(list.sort, n, trials)
    print(f"mergesort: {time_merge:.3f} s, \t .sort(): {time_py:.5f} s")


def mergesort(arr):
    """ sorts a list of comparable elements into increasing order. """
    work = [0]*len(arr)
    msort(0, len(arr)-1, arr, work)


def msort(j, k, arr, work):
    """ mergesort routine: sorts the sub-list in indices [j,k] of arr."""
    if j == k:  # trivial case
        return

    if j == k + 1:  # a larger base case
        if arr[k] < arr[j]:
            arr[j], arr[k] = arr[k], arr[j]

    # divide and sort step
    m = (j+k)//2
    msort(j, m, arr, work)
    msort(m+1, k, arr, work)

    # merge step for [j,k]
    p = j
    q = m + 1
    n = j
    while p <= m and q <= k:
        if arr[p] < arr[q]:
            work[n] = arr[p]
            p += 1
        else:
            work[n] = arr[q]
            q += 1
        n += 1

    if p <= m:
        arr[n:k+1] = arr[p:m+1]
    arr[j:n] = work[j:n]


