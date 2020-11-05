# Solve a boundary value problem using finite differences
# Example of the Thomas algorithm for solving tri-diagonal systems
# and typical usage of numpy linear algebra basics
import numpy as np
import matplotlib.pyplot as plt


def trisolve(bands, rhs):
    """ Uses Gaussian elimination to solve system a*x = rhs.
        Arguments:
            bands - the n x 3 array of bands for the matrix a
            rhs   - the rhs vector (a length n np.array)
        Returns:
            x - a new np.array (same shape as rhs) solving a*x = rhs

        Format: The array band must list the non-zero entries of a as follows:
        bands[k] = [pk, qk, rk], where
        a = [p0, q0, 0, ...    0
             r1, p1, q1, 0 ... 0
             0, r_2, p2_ q_2 ...
        The unused `padding' values are bands[0, 0] and bands[n-1, 2]
    """
    x = np.zeros(rhs.shape)
    n = bands.shape[0]

    d = np.zeros(n)   # diagonal of U
    ell = np.zeros(n)  # lower diagonal of L (multipliers)

    # to match notation from lecture (note: numpy slices don't copy!)
    # [you could also `plug this into' the algorithm directly]
    p = bands[:, 0]  # -1 diag
    q = bands[:, 1]  # center diag
    r = bands[:, 2]  # +1 diag

    # LU reduction, forward solve (Lz = b), store in x
    d[0] = q[0]
    x[0] = rhs[0]
    for j in range(1, n):
        ell[j] = p[j]/d[j-1]  # get multiplier
        d[j] = q[j] - ell[j]*r[j-1]  # reduce row
        x[j] = rhs[j] - ell[j]*x[j-1]  # reduce b (forward solve)

    # back solve (Ux = z), with overwriting
    x[n-1] = x[n-1]/d[n-1]
    for j in range(n-2, -1, -1):
        x[j] = (x[j] - r[j]*x[j+1])/d[j]

    return x


def build_fd(h, n, bc, f):
    """ Create a matrix/rhs vector in banded form for
        y'' - q(x)*y in [0, b] (Example from lecture for ODE).
        Solves for interior values y_1, ... y_(n-1) """

    # entries -1, 2+h^2, -1 on diagonals
    # rhs has entries -h^2*f(xk), plus boundary terms
    a = np.zeros((n-1, 3))
    r = np.zeros(n-1)

    # you can simplify a bit using some list comprehensions for columns;
    # the for loop is for clarity (can generalize e.g. to y'' - q(x)y)))
    for k in range(1, n):  # for each mesh point x_k...
        xk = h*k
        a[k-1, :] = [-1, 2 + h**2, -1]  # update the correct row
        r[k-1] = -h**2*f(xk)

    r[0] += bc[0]  # fix boundary conditions
    r[n-2] += bc[1]

    # NOTE: a[0, 0] and a[n-1, 2] are set here,
    #       but their values *are not used*

    return a, r


if __name__ == "__main__":
    n = 40
    """ Solve y'' - y = x with y(0) = 1 and y(1) = e -1 """

    def f(x):
        return x

    def exact(x):
        return np.exp(x) - x

    # get the linear system to solve
    h = 1.0/n
    bc = (1, np.e-1)
    mat, rhs = build_fd(h, n, bc, f)

    # now solve the linear system and add endpoints back in
    u = np.zeros(n+1)
    u[1:n] = trisolve(mat, rhs)  # set interior values
    u[0] = bc[0]  # add boundary values
    u[n] = bc[1]

    x = np.linspace(0, 1, n+1)
    y = exact(x)
    merr = np.max(np.abs(y - u))

    plt.figure()
    plt.plot(x, u, '.-k', x, y, '--r')
    plt.show()
    print(f"{n} pts: max err = {merr:.2e}")
