# Heat equation, using method of lines
import matplotlib.pyplot as plt
import numpy as np
import time


def rk4(func, interval, y0, h, skip=1):
    """ RK4 method, to solve the system y' = f(t,y) of m equations
        Inputs:
            f - a function returning an np.array of length m
         a, b - the interval to integrate over
           y0 - initial condition (a list or np.array), length m
           h  - step size to use
        Returns:
            t - a list of the times for the computed solution
            y - computed solution; list of m components (len(y[k]) == len(t))
    """
    y = np.array(y0)
    t = interval[0]
    tvals = [t]
    yvals = [y.tolist()]  # y[j][k] is j-th component of solution at t[k]
    it = 0
    while t < interval[1] - 1e-12:
        f0 = func(t, y)
        f1 = func(t + 0.5*h, y + 0.5*h*f0)
        f2 = func(t + 0.5*h, y + 0.5*h*f1)
        f3 = func(t + h, y + h*f2)
        y += (1.0/6)*h*(f0 + 2*f1 + 2*f2 + f3)
        t += h
        it += 1
        if (it % skip == 0):
            yvals.append(y.tolist())
            tvals.append(t)

    return np.array(tvals), np.array(yvals)


def heat_func(t, u, coeff, ul, ur):
    """ ODE function for method of lines to solve
        u_t = beta*u_{xx},   u(0) = ul,  u(L) = ur

        the input u contains *interior* points only,
        and coeff = beta*dt/dx^2
    """
    m = u.shape[0]  # number of active points
    du = np.zeros(m)
    for j in range(1, m-1):
        du[j] = coeff*(u[j+1] - 2*u[j] + u[j-1])

    # boundary cases
    j = 0
    du[j] = coeff*(u[j+1] - 2*u[j] + ul)
    j = m-1
    du[j] = coeff*(ur - 2*u[j] + u[j-1])

    return du


def heat_solve(ic, beta, dt, dx, ul, ur, tfinal, skip=10):
    """ solve the Dirichlet problem for the heat equation
        u_t = beta*u_xx,   u(0) = ul,  u(1) = ur
        with initial condition ic(x).

        **Note: returns only the interior points (the boundary points
                would have to be added separately; not done here)

        skip = save every this # of frames in output.
    """
    x = np.linspace(0, 1, round(1/dx)+1)
    n = len(x) - 1
    u_init = ic(x[1:n])  # set u to compute (only interior points)

    coeff = beta/dx**2

    def odef(t, u):
        return heat_func(t, u, coeff, ul, ur)

    t, u_interior = rk4(odef, [0, tfinal], u_init, dt, skip)  # interior points
    return t, x[1:n], u_interior


def initial(x):
    return x*(1-x)


if __name__ == "__main__":
    beta = 0.25
    ul = 1
    ur = 0
    dx = 0.02
    dt = 0.35*dx**2/beta
    tfinal = 0.5

    # note: only interior points are included here;
    # the (known) boundary points could be added in for the plot.
    t, x, u = heat_solve(initial, beta, dt, dx, ul, ur, tfinal, 10)
    frames = np.linspace(0, t.shape[0]-1, 20)
    plt.figure()
    for k in frames:
        plt.plot(x, u[int(k), :])
        plt.xlabel('x')
        plt.ylabel('u')
        plt.ylim([0, 1.1])
        plt.title('t={:.3f}'.format(t[int(k)]))
        plt.show()
        time.sleep(0.25)
