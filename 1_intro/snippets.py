"""
Math 260, Fall 2020
some code snippets from lecture
"""


def mut_examples():
    """ assignment examples (for lists) """
    b = [1]
    c = [2]
    b = c
    c = [3]
    print('Example 1:')
    print(b, c)

    b = [1, 2]
    b[0] = b
    b[0][1] = b[0]
    print('Example 2:')
    print(b)

    row = [1, 2]
    b = [row, row]
    b[0][0] = 7
    print('Example 3:')
    print(b)

    row = [1,2]
    b = [[0,0],[0,0]]
    for k in range(2):
        b[0][k] = row[k]
        b[1][k] = row[k]
        b[0][0] = 7
    print('Example 4:')
    print(b)
