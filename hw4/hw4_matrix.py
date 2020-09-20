""" Matrix class. Note that I've put the deepcopy option into the constructor,
so that one can make a deepcopy of mat using mat2 = Matrix(mat).
"""


class Matrix:

    def __init__(self, arg, deepcopy=False):
        if type(arg) == tuple:
            self.mat = [[0 for k in range(arg[1])] for j in range(arg[0])]
        elif type(arg) == list:
            if deepcopy:
                self.mat = [arg for row in arg]
            else:
                self.mat = arg
        else:
            raise TypeError("Invalid input to Matrix constructor.")

        self.m = len(self.mat)
        self.n = len(self.mat[0])

    def __setitem__(self, ind, val):
        self.mat[ind[0]][ind[1]] = val

    def __getitem__(self, ind):
        return mat[ind[0]][ind[1]]

    def __repr__(self,):
        s = ""
        for j in range(self.m):
            s += str(self.mat[j]) + "\n"
        return s

    def __add__(self, y):
        z = Matrix((self.m, self.n))
        for j in range(self.m):
            for k in range(self.n):
                z.mat[j][k] = self.mat[j][k] + y.mat[j][k]
        return z

    def __iadd__(self, y):
        for j in range(self.m):
            for k in range(self.n):
                self.mat[j][k] += y.mat[j][k]
        return self  # convention: += should return self

    def __sub__(self, y):
        z = Matrix((self.m, self.n))
        for j in range(self.m):
            for k in range(self.n):
                z.mat[j][k] = self.mat[j][k] - y.mat[j][k]
        return z

    def __eq__(self, y):
        return self.mat == y.mat

    def size(self):
        return (self.m, self.n)


if __name__ == "__main__":
    mat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mat[(0, 1)] = 77
    print(mat)

    mat2 = Matrix((3, 3))
    mat2[(1, 1)] = 7

    a = mat + mat2
    print(a)
