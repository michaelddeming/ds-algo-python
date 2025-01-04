"""Suppose that x and y are references to nodes of circularly linked lists,
although not necessarily the same list. Describe a fast algorithm for telling
if x and y belong to the same list."""
class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None

def in_same_cll(x, y):

    if x is None or y is None:
        return False

    x_current =  x
    while x_current.next != y:

        if x_current.next == x:
            return False
        x_current = x_current.next

    return True


n_1 = Node("A")
n_2 = Node("B")
n_1.next = n_2
n_3 = Node("C")
n_2.next = n_3
n_4 = Node("D")
n_3.next = n_4
n_5 = Node("E")
n_4.next = n_5
n_6 = Node("F")
n_5.next = n_6
n_6.next = n_1

print(in_same_cll(n_1,n_5))
