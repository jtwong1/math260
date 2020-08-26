"""
File I/O example
@author: jtwong
"""
import numpy as np


def write_dfile(x, y, fname):
    """ writes (x,y) data to a file in two columns"""
    n = len(x)
    fp = open(fname, 'w')
    fp.write(f'{n}\n')
    for k in range(n):
        line = "{:.4f}, {:.8f}\n".format(x[k], y[k])
        fp.write(line)

    fp.close()


def make_example(n, fname):
    """ Makes the example file for the lecture """
    x = [5*k/(n-1) for k in range(n)]
    y = [np.sin(v) for v in x]
    write_dfile(x, y, fname)


def read_dfile(fname):
    """ Reads in data from write_dfile. Simplest version.
        This is *not* a safe implementation (to be revisited...)"""
    fp = open(fname, 'r')
    line = fp.readline()
    n = int(line)
    x = [0]*n
    y = [0]*n
    k = 0
    line = fp.readline()
    while line:  # empty -> False, otherwise true
        # python knows to strip whitespace, e.g. float('  1.0\n') works
        words = line.split(',')
        x[k] = float(words[0])
        y[k] = float(words[1])
        line = fp.readline()
        k += 1

    fp.close()

    return x, y


def read_dfile2(fname):
    """ using readlines to get all lines first"""
    fp = open(fname, 'r')
    lines = fp.readlines()
    n = int(lines[0])
    x = [0]*n
    y = [0]*n
    for k in range(1, len(lines)):
        words = lines[k].split(',')
        x[k-1] = float(words[0])
        y[k-1] = float(words[1])

    fp.close()
    return x, y


def read_dfile3(fname):
    """ ... and with all the tricks ..."""
    with open(fname, 'r') as fp:
        n = int(fp.readline())
        x = [0]*n
        y = [0]*n
        for k, line in enumerate(fp):  # slick way to iterate over lines of f
            words = line.split(',')
            x[k], y[k] = [float(w) for w in words]

    return x, y

