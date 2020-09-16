# recursion examples from lecture


def fact(n):
    """ factorial, printing to see execution order """
    print(f"fact({n}) call")
    if n == 0:  # base
        # raise(Exception())  # (to show the stack at the base case)
        return 1
    elif n < 0:
        raise(ValueError("Invalid: negative n!"))

    v = n*fact(n-1)
    print(f"fact({n}) returns {v}")
    return v


def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


if __name__ == "__main__":
    v = fact(5)
    print(v)

    # factorial(3000)  # RecursionError!
