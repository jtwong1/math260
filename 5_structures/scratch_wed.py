""" space for lecture code """

class Foo:
    """ example class with some instance vars """

    def __init__(self):
        self.bar = 1
        self.c = 2


def func(a, b, c=4, **kwargs):
    """ keyword arguments (with a dictionary) example) """
    for k in kwargs.keys():
        print("you entered {}={}".format(k, kwargs[k]))


if __name__ == "__main__":
     k = 5
     for k in range(k, 10):
         print(k)
