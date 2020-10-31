# Partial solutions for HW 7
# (some sections omitted that are used in HW 8)

import numpy as np
from numpy import random
import matplotlib.pyplot as plt
from scipy import sparse

# TODO
# - fix the stopping criterion


def print_ranks(ranks, names, top=np.inf):
    """ prints the ranks of the nodes given the stationary distribution
        Arguments:
            ranks - the stationary distribution
        names - the names of the nodes
        top   - if positive, print only this many pages (from #1)
    """
    pairs = [(name, rank) for name, rank in zip(names.values(), ranks)]
    pairs.sort(key=lambda t: t[1], reverse=True)  # desc. sort by second entry

    for k in range(min(top, len(ranks))):
        print("#{}: {} ({:.3f})".format(k+1, *(pairs[k])))


def pt_sparse(adj, n):
    """ compute the (sparse) P^T from the adjacency list """
    total = sum((len(a) for a in adj.values()))  # total number of vertices
    r = [0]*total
    c = [0]*total
    data = [0]*total
    k = 0

    for i in range(n):
        if i not in adj:  # skip nodes with no links
            continue
        ell = len(adj[i])
        for neigh in adj[i]:
            r[k], c[k] = neigh, i  # reverse i,j due to transpose
            data[k] = 1/ell
            k += 1

    pt = sparse.coo_matrix((data, (r, c)), shape=(n, n))
    pt.tocsr()
    return pt


def ranking_sparse(mat, alpha, steps=100):
    """ Power method for pagerank, sparse-matrix friendly.
        Arguments:
            mat - the transpose of the transition matrix (P^T), either
                    an np.array (2d) or a sparse matrix.
            steps - the number of steps to take
            alpha - the teleport parameter (<1, but close to 1)
        Returns:
            x - the stationary distribution (the page rank)
    """
    n = mat.shape[0]
    x = np.random.rand(n)
    x /= sum(x)
    for it in range(steps):
        x = alpha*mat.dot(x)
        x += (1-alpha)/n  # add in the teleport part manually
        x /= sum(x)     # note: x + scalar adds scalar to each component of x
    return x


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


if __name__ == "__main__":
    adj, names = read_graph_file('california.txt')
    n = len(names)
    pt = pt_sparse(adj, n)
    x = ranking_sparse(pt, 0.95, 400)
    print_ranks(x, names, 10)
