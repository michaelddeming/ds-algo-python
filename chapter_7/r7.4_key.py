""" Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L given references only to x and y. Repeat this exercise for the case when L is a doubly linked list. Which algorithm
takes more time?"""


class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"

def singly_swap_nodes(head, node_x, node_y):
    
    

    current_node = head
    while current_node.next != node_x:
        current_node = current_node.next
    val_before_x = current_node


    current_node = head
    while current_node.next != node_y:
        current_node = current_node.next
    val_before_y = current_node

    node_y.next, node_x.next = node_x.next,node_y.next

    if node_x != head:
        val_before_x.next = node_y
    
    if node_y != head:
            val_before_y.next = node_x


# not all edge cases met, question leaves room for interpretation

def print_sll(head):
    while head:
        print(head.data)
        head = head.next

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

node = n_5


singly_swap_nodes(n_1, n_3, node)


print_sll(n_1)





    




