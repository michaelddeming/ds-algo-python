"""Describe a recursive algorithm that counts the number of nodes in a singly linked list."""

class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"
    

def count_nodes(head_node: object) -> int:

    if head_node == None: #edge case 
        return 0
    
    if head_node.next == None: #base case 
        return 1
    
    return 1 + count_nodes(head_node.next)


n = None
n_1 = Node(1)
n_2 = Node(2)
n_1.next = n_2
n_3 = Node(3)
n_2.next = n_3
n_4 = Node(4)
n_3.next = n_4
n_5 = Node(5)
n_4.next = n_5

print(count_nodes(n_1))


