# .py version of the jupyter notebook
# (the notebook or lecture slides have the relevant explanation)

import numpy as np
import matplotlib.pyplot as plt


# 1. linear convergence example (semi-log plot):
def linear_ex():
    n = np.arange(5, 201, dtype=float)  # n-values (as floats)
    seq = 2**(-n) + 100*3**(-n)  # use vectorized arith.

    fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    plt.subplot(121)
    plt.title("plain plot (not so useful)")
    plt.plot(n, seq, '--k')
    plt.xlabel('$n$')
    plt.ylabel('$a_n$')

    plt.subplot(122)
    plt.title("semi-log plot: now ~linear!")
    plt.semilogy(n, seq, '--k')
    plt.xlabel('$n$')
    plt.ylabel('$a_n$')
    fig.tight_layout()


# 2. semilog(Y) vs. plot of log(y) example:
def log_vs():
    n = np.arange(5, 201, dtype=float)
    seq = 2**(-n) + 100*3**(-n)

    fig, ax = plt.subplots(1, 2, figsize=(7.5, 3))
    plt.subplot(121)
    plt.plot(n, np.log10(seq), '--k')
    plt.ylabel('$log(a_n)$')
    plt.subplot(122)
    plt.title('semilog')
    plt.semilogy(n, seq, '--k')
    plt.ylabel('$a_n$')
    fig.tight_layout()


# 3. log-log plot (order-p convergence)

def loglog_ex():
    powers = np.arange(1, 10, dtype=float)
    n = 2**powers

    seq = 1/n**3 + 2/n**4

    fig, ax = plt.subplots(1, 2, figsize=(7.5, 3))
    plt.subplot(121)
    plt.title("plain plot (not so useful)")
    plt.plot(n, seq, '--k')
    plt.xlabel('$n$')
    plt.ylabel('$a_n$')

    plt.subplot(122)
    plt.title("log-log plot - linear!")
    plt.loglog(n, seq, '.-k')
    plt.xlabel('$n$')
    plt.ylabel('$a_n$')
    fig.tight_layout()

    # now let's add a reference line of slope -3:
    ref = 10/n**3  # build C/n^3 line to plot
    # (just make sure it doesn't overlap with seq too much)
    plt.plot(n, ref, '--r')
    plt.legend(['$a_n$', 'slope -3'])
