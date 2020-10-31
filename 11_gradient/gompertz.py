# Example of using gradient descent to fit data to a model function
# (Gompertz model example from class)

import matplotlib.pyplot as plt
import numpy as np
from numpy import random, exp


def minimize(f, df, x0, tol=1e-6, steps=100):
    """ Gradient descent with a *very simple* line search
        Inputs:
            f - the function f(x)
            df - gradient of f(x)
            x0 - initial point
    """
    x = np.array(x0)
    it = 0
    err = 100
    while err > tol and it < steps:
        v = df(x)
        fx = f(x)
        v /= max(np.abs(v))  # normalize v to unit vector
        alpha = 1  # pick an alpha [could be different scheme for doing so!]
        while alpha > 1e-10 and f(x - alpha*v) >= fx:
            alpha /= 2
        x -= alpha*v
        err = max(np.abs(alpha*v))
        it += 1

    return x, it


# ----------- Definitions for model, least squares error ----------

def gompertz(t, r):
    """ gompertz function """
    a = r[0]
    b = r[1]
    return exp(-a*exp(-b*t))


def d_gompertz(t, r):
    """ gradient of gompertz function """
    a = r[0]
    b = r[1]
    ebt = exp(-b*t)
    base = exp(-a*ebt)
    return np.array([-base*ebt, base*a*t*ebt])


def err(r, t_ex, y_ex):
    """ Least-squares error E(r) for gompertz model """
    err = 0
    for k in range(len(t_ex)):
        err += (gompertz(t_ex[k], r) - y_ex[k])**2
    return err


def derr(r, t_ex, y_ex):
    """ gradient of E(r), as defined by err """
    derr = np.zeros(2)
    for j in range(t_ex.shape[0]):
        factor = 2*(gompertz(t_ex[j], r) - y_ex[j])
        derr += factor*d_gompertz(t_ex[j], r)
    return derr


# ----------- Build model data, calculate fit ----------

def generate_data():
    n = 100
    """ generate example data for gompertz model with some noise """
    r_true = (3, 2)  # true gompertz parameters
    t_data = np.linspace(0, 2, n)
    noise = 0.04*t_data*(2-t_data)*random.uniform(-1, 1, n)
    y_data = gompertz(t_data, r_true) + noise

    return t_data, y_data


if __name__ == '__main__':
    # get (generated) example data points
    t_data, y_data = generate_data()

    # gradient descent to estimate fit parameters
    r0 = (1.0, 1.0)
    r_model, it = minimize(lambda r:  err(r, t_data, y_data),
                           lambda r: derr(r, t_data, y_data), r0, tol=1e-4)

    y_model = gompertz(t_data, r_model)
    print('model: exp(-a*exp(-bt))')
    print('fit: a={:.4f}, b={:.4f}, iterations={}'.format(*r_model, it))

    plt.figure()
    plt.plot(t_data, y_data, '.k', t_data, y_model, '--r')
    plt.legend(["exp. data", "fit"])
    plt.show()
