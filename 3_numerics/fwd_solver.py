"""
Example code from lecture: forward substitution.
Also illustrates using a `list of rows' as a matrix
and iterating over the elements with nested for loops.
"""


def fwd_solve(a, b):
    """ fwd. substition for Lx = b,
        returning a new vector x with the solution.
    """
    n = len(b)
    x = [0]*n
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= a[i][j]*x[j]
        x[i] /= a[i][i]
    return x


def fwd_solve_inplace(a, b):
    """ in-place fwd. substitution for Lx = b,
        overwriting the solution in b
    """
    n = len(b)
    for i in range(n):
        for j in range(i):
            b[i] -= a[i][j]*b[j]
        b[i] /= a[i][i]


if __name__ == "__main__":

    # version without overwriting:
    a = [[2, 0, 0], [-1, 1, 0], [4, -1, 3]]
    b = [2, 1, 5]
    # solution: x = [1, 2, 1]

    print("Solving Ax = b...")
    x = fwd_solve(a, b)
    print("x: " + str(x))

    # version *with* overwriting:
    a = [[2, 0, 0], [-1, 1, 0], [4, -1, 3]]
    b = [2, 1, 5]

    print("Solving Ax = b (in-place)...")
    fwd_solve_inplace(a, b)
    print("x: " + str(b))  # b was overwritten with the solution
