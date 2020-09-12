""" shell for HW 4 problems: Gaussian elimination
    This code specifies the functions, inputs/outputs you need to write,
    but you don't need to use the insides I've outlined.
"""


def fwd_solve(a, b):
    """ fwd. substition for Lx = b,
        returning a new vector x with the solution.
        ***lecture version, not quite the one you need here***
    """
    n = len(b)
    x = [0]*n
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= a[i][j]*x[j]
        x[i] /= a[i][i]
    return x


def back_solve(a, b):  # (placholder; use yours)
    n = len(b)
    x = [0]*n
    ...
    return x


def ge_lu(a):
    """ LU factorization of the matrix a. Returns L and U in one matrix. """
    n = len(a)
    mat = [row[:] for row in a]  # make a copy of a

    for k in range(n-1):
        # reduce k-th column

        # with pivoting: choose the pivot element,
        # swap rows and update permutation vector.
        ...
        for i in range(k+1, n):
            # zero out (i, k) entry
            ...
            for j in range(..., ...):  # row reduction for i-th row
                ...
                # update entry in row

    return mat


# Template for version without pivoting
def linsolve(a, b):
    """ put a doc-string here describing the algorithm """
    n = len(b)
    x = [0]*n
    y = [0]*n  # optional: change code to avoid need for this intermediate vec.

    mat = ge_lu(a)
    y = fwd_solve(mat, b)
    x = back_solve(mat, y)
    return x


# Template for version with pivoting
def linsolve(a, b):
    """ put a doc-string here describing the algorithm """
    n = len(b)
    x = [0]*n
    y = [0]*n  # optional: change code to avoid need for this intermediate vec.

    mat, p = ge_lu(a)
    y = fwd_solve(mat, b, p)  # OR compute pb = P*b, then fwd_solve(mat, pb)
    x = back_solve(mat, y)
    return x


if __name__ == "__main__":

    # typical structure of linsolve call:
    a = [[1,0,0], [0,1,0], [0,0,1]]
    b = [1,2,3]
    x = linsolve(a, b)
    print(x)
