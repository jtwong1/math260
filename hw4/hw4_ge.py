"""
Homework 4 solutions: Gaussian elimination
"""


def lu_factor(a, copy=True, pivoting=True):
    """ computes the LU factorization of a using Gaussian elimination, i.e.
        lower/upper tri. L, U and permutation matrix P so that PA = LU.
        Args:
            a: the matrix to to factorize
            copy: (default: True) whether to create a copy of a or overwrite.
            pivoting: (Default: True) use partial pivoting or no pivoting.
        Returns:
            u: L and U, stored compactly in the lower/upper halves
            p: the permutation vector for the swaps
    """
    if copy:
        u = [r[:] for r in a]
    else:
        u = a  # don't copy a; overwrite

    n = len(a)
    p = [k for k in range(n)]
    for k in range(n-1):
        pivot = k
        if pivoting:
            for i in range(k+1, n):
                if abs(u[pivot][k]) < abs(u[i][k]):
                    pivot = i
            u[i], u[k] = u[k], u[i]  # swap rows
            p[i], p[k] = p[k], p[i]
        for i in range(k+1, n):
            m = u[i][k]/u[k][k]
            u[i][k] = m
            for j in range(k+1, n):
                u[i][j] -= m*u[k][j]

    return u, p  # return L and U together as u


def fwd_solve_lu(a, b, p):
    """ Solves Ly = Pb where L is stored in the lower half of a """
    n = len(b)
    x = [0]*n
    for i in range(n):
        x[i] = b[p[i]]
        for j in range(0, i):
            x[i] -= a[i][j]*x[j]
    return x


def back_solve(a, b):
    """ Solves Uy = b where U is stored in the upper half of a """
    n = len(b)
    x = [0]*n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= a[i][j]*x[j]
        x[i] /= a[i][i]
    return x


def linsolve(a, b, copy=True, pivoting=True):
    """ Solves the linear system Ax = b using Gaussian elimination.
        Args:
            a: an n x n matrix as a *list of rows*
            b: a list of length n
        Returns:
            x: the solution (as a list)
    """
    ellu, p = lu_factor(a, copy, pivoting)
    y = fwd_solve_lu(ellu, b, p)
    x = back_solve(ellu, y)
    return x


def residual(a, x, b):
    """ Calculates the residual A*x - b, returning a new list """
    n = len(b)
    res = [0]*n
    for k in range(n):
        res[k] = -b[k]
        for j in range(n):
            res[k] += a[k][j]*x[j]

    return res


if __name__ == '__main__':
    a = [[5, 7, -8, 13], [2, 4, 5, 7], [21, -13, 5, 3], [1, 2, 12, 1]]
    b = [-23, -4, 36, 10]
    # true solution: [1, -1, 1, -1]

    x = linsolve(a, b, copy=True, pivoting=True)
    max_r = max([abs(v) for v in residual(a, x, b)])
    print("Max. resid. size: {:.2e}".format(max_r))
