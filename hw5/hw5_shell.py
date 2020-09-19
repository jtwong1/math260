""" Binary tree and mergseort example code for HW 5.
Same as the lecture code, but some lecture-specific examples cut.
(See lecture code for the test examples + example of creating a tree). """
import random

# ---------------------------------
# mergesort shell
# (nothing to change in mergesort; write code in msort)


def mergesort(arr):
    """ ... put a doc-string here ..."""
    work = [0]*len(arr)
    msort(0, len(arr), arr, work)


def msort(j, k, arr, work):
    """ mergesort - recursive implementation """

    # divide and sort step
    m = (j+k)//2
    msort(j, m, arr, work)
    msort(m+1, k, arr, work)

    # merge step (you'll need the "work" array)


def test_list(n, maxval=1000):
    """ list of random integers for testing sort """
    random.seed(260)  # fix the random seed, so the list is the same each run.
    return [random.randint(0, maxval) for k in range(n)]


# ---------------------------------
# Code for binary trees
class BNode:
    """ Binary search tree node class"""

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.children = [left, right]
        self.parent = parent

    def __repr__(self):
        return "Node({})".format(self.data)


class BTree:
    """ Binary tree class (storing the root node; has member functions) """

    def __init__(self, root):
        self.root = root

    def insert(self, val):
        """ insert a new leaf node with data val"""
        node = self.root
        while node:
            p = node
            side = val > node.data
            node = node.children[side]

        p.children[side] = BNode(val, None, None, p)  # new leaf, parent p

    def find(self, val):
        """ find a node with data val """
        n = self.root
        while n and n.data != val:
            n = n.children[val > n.data]

        return n  # returns None if not found

    def remove(self, val):
        """ removes a node with data val """
        n = self.find(val)
        if not n:
            print(f"node ({val}) not found!")
            return
        else:
            self.delete(n)

    def delete(self, n):
        """ deletes the specified node (must be in the tree)"""
        left = n.children[0]
        right = n.children[1]

        print(f"Call: delete({n})")
        # Case: If the node has two children ...
        if left and right:
            while left.children[1]:  # find largest predecessor
                left = left.children[1]

            print(f"> move {left} into {n}")
            n.data = left.data  # move up the predecessor
            self.delete(left)  # ... recursively remove old node
            return

        # Case: leaf node
        if not(left or right):
            if n == self.root:
                self.root = None
            else:
                side = n.data > n.parent.data
                n.parent.children[side] = None  # cut off the node
                print("- remove leaf")
            return

        # Case: one child... first get the child...
        if left:
            child = left
        else:
            child = right

        # ...then delete.
        if n == self.root:
            self.root = child
            child.parent = None
        else:
            side = n.data > n.parent.data
            n.parent.children[side] = child
            child.parent = n.parent
            print("- remove (one side)")

        return  # nothing to return, but could have a return code for success

    def __repr__(self):
        """crude print for the tree, with each depth on one line.
           Uses * to denote None (no child for a node)"""
        level = 0
        q = [(self.root, level)]
        rep = ""
        while q:
            n, level = q.pop(0)
            if not n:
                rep += "*"
            else:
                rep += str(n.data)
                q.append((n.children[0], level+1))
                q.append((n.children[1], level+1))
            rep += " "
            if q and q[0][1] > level:
                rep += "\n"

        return rep
