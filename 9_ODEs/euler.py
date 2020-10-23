# Euler's method (scalar ODE) example code
import numpy as np
import matplotlib.pyplot as plt


def fwd_euler(f, a, b, y0, h):
    """ Forward Euler with fixed step size using a while loop."""
    y = y0
    yvals = [y]
    tvals = [a]
    t = a  # set current time
    while t < b - 1e-12:  # (avoids rounding error where t misses b slightly)
        y += h*f(t, y)
        t += h
        yvals.append(y)
        tvals.append(t)

    return tvals, yvals


def ode_func(t, y):
    """ ode function for lecture example (y' = 2ty) """
    return 2*t*y


def sol_true(t, y0):
    """ true solution for the example, given y(0) = y0 """
    return y0*np.exp(t**2)


def example_plot():
    """ Solve y' = 2ty, y(0) = 1 using Euler's method.
        (Example from lecture with a plot)
    """
    b = 1
    h = 0.01
    y0 = 1
    t, y_approx = fwd_euler(ode_func, 0, b, y0, h)
    t_true = np.linspace(0, b, 200)  # use a finer grid to plot true solution
    y_true = sol_true(t_true, y0)  # use numpy vector math

    # example print at t=b
    print("{:.2f} \t {:.2f}".format(t[-1], y_approx[-1]))

    plt.figure()
    plt.plot(t, y_approx, '.--r')
    plt.plot(t_true, y_true, '-k')


# -----------------
# Examples from lecture...
def convergence_ex():
    """ Solve y' = 2ty, y(0) = 1 using Euler's method.
        Use the true solution to compute the max error,
        and show that it is O(h)
    """
    hvals = [(0.1)*2**(-k) for k in range(8)]
    y0 = 1
    b = 1

    err = [0]*len(hvals)
    for k in range(len(hvals)):  # err[k] is the max error given spacing h[k]
        t, u = fwd_euler(ode_func, 0, b, y0, hvals[k])

        # compute errors at each t (point_errs), then max. error
        # (use zip/list comprehension trick to iterate over t and u)
        point_errs = [abs(sol_true(t1, y0) - u1) for t1, u1 in zip(t, u)]
        err[k] = max(point_errs)  # max error

    # ... or use the log-log plot:
    plt.figure()
    plt.loglog(hvals, hvals, '--r')
    plt.loglog(hvals, err, '.--k')
    plt.legend(['slope 1', 'max. err.'])
    plt.xlabel('$h$')


def endpoint_err_ex():
    """ example of endpoint sample + ratios to estimate order """
    m = 8
    hvals = [(0.1)*2**(-k) for k in range(m)]
    y0 = 1
    b = 1

    endval = [0]*m
    ratios = [0]*m
    for k in range(m):
        t, u = fwd_euler(ode_func, 0, b, y0, hvals[k])
        endval[k] = u[-1]
        if k >= 2:
            ratios[k] = (endval[k]-endval[k-1])/(endval[k-1] - endval[k-2])

    print("h \t \t u(b) \t \t ratio \t \t p est.")
    for k in range(m):
        p = -np.log2(ratios[k])
        print(f"{hvals[k]:.2e} \t {endval[k]:.4f}", end="")
        if k >= 2:
            print(f"\t {ratios[k]:.2f} \t {p:.2f}")
