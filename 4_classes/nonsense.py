""" An example of overriding functions inherent to objects
    to do confusing things. Not recommended.
"""


class Mess:
    initialized = False

    def __init__(self):
        self.v = 1
        self.w = 2
        self.initialized = True

    # this defines the `dot' behavior (like obj.var)
    # you *can*, but should almost never override it.
    def __getattr__(self, name):
        if name[0] != '_':
            print(name + ' not found!')

    # this defines dots on the left of equals: obj.var = value
    def __setattr__(self, name, value):  # don't do this
        if name[0] != '_':
            if(self.initialized and name[0] == 'z'):
                print("Ignored! New instance vars. can't start with z!")
            else:
                self.__dict__[name] = value

    # defines function-like behavior: obj(inputs)
    def __call__(self, x):
        print(x + self.v + self.w)

    # __del__ is called when an object is deleted
    def __del__(self):
        print('Goodbye!')


# --------------------------------
# Examples of the overrides:


def ex_del():
    a = Mess()
    print(a.v)
    # now a leaves scope -> deleted


def ex_call():
    a = Mess()
    a(5)  # as defined, prints 5 + 1 + 2


def ex_dot_attr():
    a = Mess()
    a.foo  # a has no member foo - overriden getattr kicks in here
    a.bar = 5
    a.zoom = 1234  # overriden setattr says no here: z's not allowed!
