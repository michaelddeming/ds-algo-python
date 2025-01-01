"""Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None."""

class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


def second_to_last_node(node):

    # edge case, if node provided
    if node == None or node.next == None:
        return None # if there is one or fewer nodes, we dont have a 2nd to last node
    
    next_node = node.next

    if next_node.next is None: #base case met, tail 
        return node


    return second_to_last_node(next_node)


n_1 = Node(1)
n_2 = Node(2)
n_1.next = n_2
n_3 = Node(3)
n_2.next = n_3
n_4 = Node(4)
n_3.next = n_4
n_5 = Node(5)
n_4.next = n_5

print(second_to_last_node(n_1))


