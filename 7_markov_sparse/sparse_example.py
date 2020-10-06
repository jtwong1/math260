# a few sparse matrix examples using the sparse package
import numpy as np
from scipy import sparse
from numpy import random
from time import perf_counter as timer


def rat_matrix(n, p):
    numel = 3*n-2
    s = 1-2*p
    row = [0]*numel
    col = [0]*numel
    val = [0]*numel
    row[0:2] = [0, 0]
    col[0:2] = [0, 1]
    val[0:2] = [s, p]
    pos = 2
    for j in range(1, n-1):
        row[pos:pos+3] = [j, j, j]
        col[pos:pos+3] = [j-1, j, j+1]
        val[pos:pos+3] = [p, s, p]
        pos += 3
    row[-2:] = [n-1, n-1]
    col[-2:] = [n-2, n-1]
    val[-2:] = [p, s]

    mat = sparse.coo_matrix((val, (row, col)), shape=(n, n))
    return mat


def mult_test(n):
    """ Test example: sparse/dense matrix multiply. NOTE: test only
    n <= 1000 to avoid *very large* arrays for the dense matrix
    """
    mat = rat_matrix(n, 0.25)
    mat.tocsr()  # convert to (efficient) CSR format
    x = random.uniform(0, 1, n)

    mat_dense = mat.toarray()

    start = timer()
    y1 = mat.dot(x)
    time_sparse = timer() - start

    start = timer()
    y2 = mat_dense.dot(x)
    time_dense = timer() - start

    print(f"Matrix multiply, n={n}:")
    print(f"Sparse time: {time_sparse:.1e}s")
    print(f"Dense time: {time_dense:.1e}s")
    print("Ratio, dense/sparse: {:.1f}".format(time_dense/time_sparse))
    print("equality check: {}".format(np.max(np.abs(y1 - y2)) < 1e-14))


def sparse_example1():
    """ Simple example: a matrix with entries in an x-shape. """
    n = 5
    # list row/col indices and values: the (r[k],c[k]) entry has value data[k]
    row = [0, 4, 0, 4, 1, 3, 1, 3, 2]   # row indices
    col = [0, 4, 4, 0, 1, 3, 3, 1, 2]   # col indices
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # data (values)

    # function call to make the matrix in COOrdinate form:
    # note that the first arg. is a tuple: (data, (row indices, col indices))
    mat = sparse.coo_matrix((data, (row, col)), shape=(n, n))
    print(mat.toarray())
    return mat


def sparse_example2():
    """ Example:  build a sparse matrix with 0, 1, 4, ... (n-1)^2
    on the diagonal and 1 1 1 1 ... 1 one entry above the diagonal
    NOTE: you could be more efficient and allocate r,c first here
    """
    n = 5
    row = []
    col = []
    data = []
    for k in range(n-1):
        row.extend([k, k])  # add entries for (k,k) and (k,k+1)
        col.extend([k, k+1])
        data.extend([k**2, 1])

    row.append(n-1)  # lower right entry (n,n)
    col.append(n-1)
    data.append((n-1)**2)

    mat = sparse.coo_matrix((data, (row, col)), shape=(n, n))
    print(mat.toarray())
    return mat
