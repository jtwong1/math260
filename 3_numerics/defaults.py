def glue(elements, base=[]):
    """ - with base specified, adds elements to the end of base
        - with default argument, creates an ampty list, then
            adds elements to it and returns the reference
        (DOES NOT DO AS INTENDED!)"""
    base.extend(elements)
    return base


if __name__ == "__main__":
    a = [3, 4]
    b = glue(a)

    base = [1, 2]
    glue(a, base)

    oops = glue(a)
    b[0] = 7


def func(a, record=[]):
    """ shell for a function that processes a value, and keeps a record
        of all inputs sent to this function.
    """
    # ... do something with  a ...
    record.append(a)
    return a, record


def record_example():
    """ Example of use of func """
    r = func(1)[0]
    s = func(2)[0]
    t, record = func(3)

    # func is called three times, adding to record each time
    print(record)
