# Partial solutions for HW 7
# (some sections omitted that are used in HW 8)

import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def norm2(v):
    return np.sqrt(v.dot(v))


def normi(v):
    return np.max(np.abs(v))


# ------------------------------------------------------------
# power method exercise
def power_method_test(a, true_v, tol=1e-8, max_steps=100):
    """ simple implementation of the power method, using a fixed
        number of steps. Computes the largest eigenvalue and
        associated eigenvector.

        Args:
            a - the (n x n) matrix
            steps - the number of iterations to take
        Returns:
            x, r - the eigenvector/value pair such that a*x = r*x
    """
    x = random.rand(a.shape[0])
    x = np.ones(3)
    it = 0
    err = tol
    true_err = []

    while err >= 0*tol and it < max_steps:
        q = np.dot(a, x)
        r = x.dot(q)
        tmp = q/norm2(q)
        err = normi(x - tmp)
        x[:] = tmp[:]
        it += 1
        true_err.append(min(normi(x - true_v), normi(x + true_v)))

    return x, r, true_err


def q1():
    a = np.array([[0.0, 1, 0], [0, 0, 1], [6, -11, 6]])
    # eigenvalues: 3, 2, 1
    # eigenvalues/vectors:
    v1 = np.array([1, 3, 9])

    x, r, err = power_method_test(a, v1/norm2(v1), 1e-5, 40)
    np.set_printoptions(precision=6)  # set num. of displayed digits
    plt.figure(figsize=(4, 3.2))
    nvals = range(0, len(err))
    plt.semilogy(nvals, err, '.-k')
    ref_line = [(2/3)**n for n in nvals]
    plt.semilogy(nvals, ref_line, '--r')
    plt.xlabel('$n$')
    plt.ylabel('err')
    plt.legend(['error in evec', 'slope -2/3'])
    plt.savefig('q1.pdf', bbox_inches='tight')


# ------------------------------------------------------------
# pagerank

def stationary(pt, tol=1e-6, max_steps=400):
    """Power method to find stationary distribution.
       Given the largest eigenvalue is 1, finds the eigenvector.
    """
    x = random.rand(pt.shape[0])  # random initial vector
    tmp = np.zeros(pt.shape[0])
    x /= sum(x)
    it = 0
    err = 10
    while it < max_steps and err > tol:
        tmp = np.dot(pt, x)
        err = normi(x - tmp)
        x[:] = tmp[:]
        it += 1
    return x, it


def pagerank_small(alpha):
    """ small pagerank example from lecture (four nodes) """
    pass
	# (omitted)

# ------------------------------------------------------------
# file IO

def read_graph_file(fname, node_pre='n', adj_pre='a', edge_pre='e'):
    """ First, it reads lines with prefix n (for node) of the form
        n k name    and stores a dict. of names for the nodes.
        Reads adj. matrix data from a file, returning the adj. list.
        Format: A line starting with...
            - 'n' is read as  n k name  (the node's name)
            - 'e' is read as e k m (an edge k->m)

        Returns:
            adj - the adj. dictionary, with adj[k] -> list of neighbors of k
            names - the dictionary of node names, if they exist

        NOTE: the adj. list does not store dead nodes (with no links)
    """
    adj = {}
    names = {}

    with open(fname, 'r') as fp:
        for line in fp:
            parts = line.split(' ')
            if len(parts) < 2:
                continue
            node = int(parts[1])
            if parts and parts[0][0] == 'n':
                names[node] = parts[2].strip('\n')
            elif parts and parts[0][0] == 'e':
                v = int(parts[2])
                if node not in adj:
                    adj[node] = [v]
                else:
                    adj[node].append(v)

    return adj, names
