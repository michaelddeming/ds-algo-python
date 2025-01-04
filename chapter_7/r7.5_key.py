"""Implement a function that counts the number of nodes in a circularly
linked list."""

# CLL: Head --> Node --> Tail --> Head

class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"
    
def count_cll_nodes(start_node):

    count = 1

    if start_node is None:
        return 0

    current_node = start_node
    while current_node.next != start_node:
        count += 1
        current_node = current_node.next
    return count


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

print(count_cll_nodes(n_1))

