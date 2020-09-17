""" Node class (for a tree) and depth/breadth first search examples.
    Example code in main at the bottom.

    A crude print-tree function is also provided for viewing the tree.
"""


class Node:

    def __init__(self, data, children):
        self.data = data
        self.children = children.copy()  # shallow copy

    def __repr__(self):
        return "n({})".format(self.data)


def print_tree(root):
    """ crude print function; each line represents nodes at a given depth,
        and children of each node are separated by ||s.
        Uses a breadth-first search to get the right ordering to print.
    """
    q = [root, "*"]  # * is a fake node that signifies a line break
    while len(q) > 1:
        n = q.pop(0)
        if n == "*":
            print("")
            q.append("*")
        elif n == "|":
            print("| ", end="")
        else:
            print(str(n) + " ", end="")
            q.extend(n.children)
            q.append("|")


def example():
    """ Tree example from lecture:
           0
         |  \
       1     2
     / | \   \
    3 4  5   6
    """
    n = [Node(k, []) for k in range(7)]

    n[0].children = [n[1], n[2]]
    n[1].children = [n[3], n[4], n[5]]
    n[2].children = [n[6]]

    return n[0]


def dfs_rec(val, root):
    """ recursive variant: depth-first search """
    if(root.data == val):
        return root

    for child in root.children:
        t = dfs_rec(val, child)
        if t:  # if t != None
            return t

    return None


def dfs(val, root):
    """ stack variant: depth-first search """
    stack = [root]
    it = 0
    while stack:
        print("it=" + str(it) + " : " + str(stack))
        n = stack.pop()
        if n.data == val:
            return n
        stack.extend(n.children)
        it += 1

    return None


def bfs(val, root):
    """ with a quee: breadth-first search """
    q = [root]
    it = 0
    while q:
        print("it=" + str(it) + " : " + str(q))
        n = q.pop(0)
        if n.data == val:
            return n
        q.extend(n.children)
        it += 1

    return None


if __name__ == "__main__":
    root = example()
    val = 3
    n = dfs(val, root)
    # n = bfs(val, root)
    if n:
        print(f"found {val} at node {n}")
    else:
        print(f"Value {val} not found!")