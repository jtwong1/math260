# Lecture code: bee example.
# The power method for computing a stationary distribution,
# plus code for choosing a move from a state to the next.

import numpy as np
from numpy.random import uniform, rand   # for a random number


# --------------------------------------------------------
# Direct simulation of bees to estimate stationary distribution
# (same algorithm as the midterm code)
def choose(probs):
    """ Example code (from lecture, edited) to pick a choice.
        given choices 0, ..., n-1 with probs p0, .. p_(n-1),
        picks one with the appropriate probability.
    """
    r = uniform(0, 1)
    total = probs[0]
    k = 0
    while r > total:
        k += 1
        total += probs[k]
    return k


def bee_simulation(nb, steps):
    p = np.array([[0.5, 0.5, 0.0],
                  [0.5, 0.0, 0.5],
                  [0.7, 0.3, 0]])

    bees = [1 for k in range(nb)]
    bins = [0]*len(p)

    for k in range(steps):
        for j in range(nb):
            probs = p[bees[j]]
            bees[j] = choose(probs)

    for j in range(nb):
        bins[bees[j]] += 1

    for k in range(len(bins)):
        bins[k] /= nb

    return bins


# --------------------------------------------------------
# Stationary distribution calculation from theory
def stationary(pt, steps):
    """Power method to find stationary distribution.
       Given the largest eigenvalue is 1, finds the eigenvector.
    """
    x = rand(pt.shape[0])  # random initial vector
    x /= sum(x)  # normalize (not necessary, in theory!)
    for it in range(steps):
        x = np.dot(pt, x)
    return x


def calculate_bees():
    """ stationary distribution for the bee example, closed window,
        computed two ways (simulation and via eigenvalues [the right way])
    """
    pt = np.array([[0.5, 0.5, 0.7],
                  [0.5, 0.0, 0.3],
                  [0.0, 0.5, 0]])
    dist = stationary(pt, 20)
    print("Stationary distribution:")
    print(dist)

    # for direct simulation
    steps = 1000
    dist_sim = bee_simulation(2000, steps)
    print(f"From simulation ({steps} steps):")
    print(dist_sim)
