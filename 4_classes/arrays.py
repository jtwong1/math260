# Operator overloading example: Vector class
# ******completed example code******

class Vector:

    def __init__(self, r):  # constructor
        if type(r) == int:
            self.arr = [0 for k in range(r)]
        else:
            self.arr = r[:]

    def __repr__(self):
        return str(self.arr)

    def __getitem__(self, k):  # arr[k]
        return self.arr[k]

    def __setitem__(self, k, val):  # arr[k] = v
        self.arr[k] = val

    def __add__(self, y):  # z <- x + y
        n = len(self.arr)
        z = Vector(n)
        for k in range(n):
            z[k] = self.arr[k] + y[k]
        return z

    def __sub__(self, y):  # z <- x - y
        n = len(self.arr)
        z = Vector(n)
        for k in range(n):
            z[k] = self.arr[k] - y[k]
        return z

    def __rmul__(self, y):
        if type(y) != float and type(y) != int:
            raise TypeError("Incorrect lvalue type!")
        n = len(self.arr)
        z = Vector(n)
        for k in range(n):
            z[k] = y*self.arr[k]
        return z

    def __mul__(self, y):
        return None


# ------- tests to run -----------

def create():  # test: creating vectors
    x = Vector([1, 2, 3])
    y = Vector([4, 5, 6])
    print("x: " + str(x))  # str uses x.__repr__
    print("y: " + str(y))


def arith():  # test : adding vectors together, etc.
    x = Vector([1, 2, 3])
    y = Vector([4, 5, 6])
    x[1] = -1
    z = x + y
    print(z)

    print(2*x + 3*y)
