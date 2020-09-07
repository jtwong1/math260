"""
Math 260, Fall 2020
Homework 2 example solution:
Binary search to find an element in a list
"""


def search(arr, x):
    """ Given a sorted array in *increasing* order, find
        the index of the element x.
        Args:
            arr: the list to search (with increasing elements)
            x: the element to match
        Returns:
            c: the index of x (or -1 if not found)
    """
    a = 0
    b = len(arr) - 1  # bracketing indices

    if x < arr[a] or x > arr[b]:
        return -1

    while a <= b:
        c = (a + b) // 2  # note *integer* division
        fc = arr[c]

        if x == fc:
            return c
        elif x < fc:
            b = c - 1
        else:
            a = c + 1

    return -1


if __name__ == "__main__":
    data = [i**2 for i in range(10)]
    x = 9
    c = search(data, x)
    print("List: " + str(data))
    print(f"Found {x} at index {c}.")