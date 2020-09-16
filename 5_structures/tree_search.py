# tree generation
class Node:

    def __init__(self, data, children):
        self.data = data
        self.children = children.copy()  # shallow copy

    def __repr__(self):
        return "n({})".format(self.data)


def example():
    n = [Node(k**2, []) for k in range(7)]

    n[0].children = [n[1], n[2]]
    n[1].children = [n[3], n[4], n[5]]
    n[2].children = [n[6]]

    return n[0]


def dfs(val, root):
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
