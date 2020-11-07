# Heat equation, using method of lines
import matplotlib.pyplot as plt
import numpy as np


def heat_solve(ic, dt, dx, beta, bc_left, bc_right, tfinal):
    """ solve the Dirichlet problem for the heat equation
        u_t = beta*u_xx,   u(0) = g(t),  u(1) = h(t)
        with initial condition ic(x).

        Note that the boundary conditions are functions of t!

        Example code from class, not really a complete routine;
        only outputs u at the final time
    """
    x = np.linspace(0, 1, round(1/dx)+1)
    u = ic(x)
    n = len(x)-1
    unew = np.zeros(n+1)
    coeff = beta*dt/dx**2

    t = 0
    u[0] = bc_left(t)
    u[n] = bc_right(t)
    while t < tfinal:

        # update interior points
        for j in range(1, n):
            unew[j] = u[j] + coeff*(u[j-1] - 2*u[j] + u[j+1])

        t += dt
        # left boundary:
        unew[0] = bc_left(t)
        unew[n] = bc_right(t)

        u[:] = unew[:]

    return t, x, u


def initial(x):  # example IC
    return x*(1-x)


def bc_left(t):  # example BC function (left)
    return 0


def bc_right(t):  # example BC function (right)
    return 0.25*np.sin(t)


if __name__ == "__main__":
    beta = 0.25
    dx = 0.02
    dt = 0.25*dx**2/beta
    tfinal = 1

    t, x, u = heat_solve(initial, dt, dx, beta, bc_left, bc_right, tfinal)
    plt.figure()
    plt.plot(x, u)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.title('t={:.3f}'.format(t))
    plt.show()
