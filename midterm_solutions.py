""" Midterm solutions. Note that there are many alternate ways to solve
the problems; the following is just one example set of solutions. """
import random


def scurry(n, start, minutes, show=True):
    """ simulates the rat moving through the line of rooms """
    pos = start
    if show:
        print("time \t room")
        print("{} \t {}".format(0, pos))
    for k in range(minutes):
        if pos == 0:
            choice = random.randint(0, 1)
        elif pos == n-1:
            choice = random.randint(-1, 0)
        else:
            choice = random.randint(-1, 1)

        pos += choice
        if show:
            print("{} \t {}".format(k+1, pos))

    return pos


def distribution(n, minutes, start, trials=10000):
    """ Calculates the distribution of rat locations after
        a certain # of minsutes, given a starting point. """
    prob_list = [0]*n

    for k in range(trials):
        pos = scurry(n, start, minutes, show=False)
        prob_list[pos] += 1

    for k in range(n):
        prob_list[k] /= trials

    return prob_list


def test_distribution():
    """ Test code for the distribution function """
    n = 9
    minutes = 60

    p_left = distribution(n, minutes, 0)[0]
    p_right = distribution(n, minutes, n-1)[0]

    print(f"prob. of being in room 0 after {minutes} min:")
    print(f"start=0: p={p_left}")
    print(f"start=n-1: p={p_right}")


# ---------------------------------------------
def toeplitz(seed):
    """ toeplitz construction, with slices """
    if len(seed) % 2 == 0:
        raise ValueError('Wrong parity for seed length!')
    n = (len(seed)+1)//2

    mat = [[0 for k in range(n)] for j in range(n)]

    for j in range(n):
        mat[j] = seed[n-1-j: 2*n-1-j]

    return mat


# --------------------------------------------------------
class Node:

    def __init__(self, data, right):
        self.data = data
        self.right = right

    def __repr__(self):
        return "N(" + str(self.data) + ")"


class Chain:

    def __init__(self, data):
        self.base = Node(data, None)

    def __repr__(self):
        current = self.base  # reference to current node
        result = ""
        while current:
            result += str(current) + "-"
            current = current.right
        return result

    def pop(self):
        popped = self.base  # node to pop
        if not popped:
            raise ValueError("Size is zero!")
        self.base = popped.right

        return popped.data

    def prepend(self, data):
        base_new = Node(data, self.base)
        self.base = base_new

    def insert(self, data, k):

        pos = 0
        current = self.base
        while pos < k and current:
            pos += 1
            current = current.right

        if not current:
            raise IndexError(f"index {k} too large!")

        current.right = Node(data, current.right)

    def attach(self, more):
        current = self.base
        while current.right:
            current = current.right

        current.right = more.base


def squares(n):
    square_chain = Chain(n**2)

    for k in range(n-1, 0, -1):
        square_chain.prepend(k**2)

    return square_chain


def chain_test():
    n = 5
    c = squares(n)
    print("pop test:")
    for k in range(n):
        print(c.pop())

    c = squares(5)
    c.insert(7, 0)
    c.insert(-1, 3)
    print(c)

    c = squares(5)
    more = squares(3)
    c.attach(more)
    print(c)
