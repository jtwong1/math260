# TEST SOLUTIONS
import random


def scurry(n, start, minutes, show=True):
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


def distribution(n, minutes, start=0, trials=10000):
    prob = [0]*n

    for k in range(trials):
        pos = scurry(n, start, minutes, show=False)
        prob[pos] += 1

    for k in range(n):
        prob[k] /= trials

    return prob


def test_dist():
    n = 8
    minutes = 100

    p1 = distribution(n, minutes, 0)
    p2 = distribution(n, minutes, n-1)

    print(p1)
    print(p2)
    print([x - y for x, y in zip(p1, p2)])


# ---------------------------------------------
def toeplitz(seed):
    if len(seed) % 2 == 0:
        raise ValueError('Wrong parity for seed length!')
    n = (len(seed)+1)//2

    mat = [[0 for k in range(n)] for j in range(n)]

    for diag in range(0, n):
        for k in range(0, n - diag):
            print(k + diag, k)
            mat[k + diag][k] = seed[n - 1 - diag]

    for diag in range(1, n):
        for j in range(0, n - diag):
            print(j, j + diag)

    mat[j][j+diag] = seed[n - 1 + diag]

    mat2 = [None]*n
    for j in range(n):
        mat2[j] = seed[n-1-j: 2*n-1-j]

    return mat, mat2


def toep_test():
    """ test for norm1: should output 10 """
    mat = [[1, 2, 0], [4, 3, -1], [-5, 2, 1], [0, 1, 3]]
    print(norm1(mat))



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
        v = self.base
        rep = ""
        while v:
            rep += str(v) + "-"
            v = v.right
        return rep

    def pop(self):
        v = self.base
        if not v:
            raise ValueError("Size is zero!")
        self.base = v.right

        return v.data

    def prepend(self, data):
        v = Node(data, self.base)
        self.base = v

    def insert(self, data, k):

        pos = 0
        v = self.base
        while pos < k and v:
            pos += 1
            v = v.right

        if not v:
            raise IndexError(f"index {k} too large!")

        v.right = Node(data, v.right)

    def attach(self, more):
        v = self.base
        while v.right:
            v = v.right

        v.right = more.base


def squares(n):
    v = Node(n**2, None)

    for k in range(n-1, 1, -1):
        v = Node(k**2, v)

    c = Chain(1)
    c.base.right = v
    return c


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
