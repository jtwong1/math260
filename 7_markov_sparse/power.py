import numpy as np
from numpy import random


def power_method(a, steps):
    """ simple implementation of the power method, using a fixed
        number of steps. Computes the largest eigenvalue and
        associated eigenvector.

        Args:
            a - the (n x n) matrix
            steps - the number of iterations to take
        Returns:
            x, r - the eigenvector/value pair such that a*x = r*x
    """
    n = a.shape[0]
    x = random.rand(n)
    it = 0
    while it < steps:  # other stopping conditions would go here
        q = np.dot(a, x)  # compute a*x
        r = x.dot(q)    # Rayleigh quotient x_k dot Ax_k / x_k dot x_k
        x = q/np.sqrt(q.dot(q))  # normalize x to a unit vector
        it += 1
    return x, r


if __name__ == "__main__":   # example from lecture (2x2 matrix)
    a = np.array([[3, 1], [0, 2]])
    evec, eig = power_method(a, 100)

    np.set_printoptions(precision=3)  # set num. of displayed digits
    print(f"Largest eigenvalue: {eig:.2f}")
    print("Eigenvector: ", evec)
