"""Describe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L'
that contains all the nodes of L followed by all the nodes of M."""

class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None

    def __str__(self):
        return f"Node({self.data})"


def combine_singly_linked_lists(L_node_head, M_node_head):

    if L_node_head == None: # edge case: if there are no nodes in the LL return None
        return M_node_head
    
    if M_node_head == None: # edge case: if there are nodes in L and none in M, return L
        return L_node_head
    
    if L_node_head.next == None: #base case 
        L_node_head.next = M_node_head
        return
    
    combine_singly_linked_lists(L_node_head.next, M_node_head)

    return L_node_head #override the return of L tail with the start of L head    
    
n_1 = Node(1)
n_2 = Node(2)
n_1.next = n_2
n_3 = Node(3)
n_2.next = n_3
n_4 = Node(4)
n_3.next = n_4
n_5 = Node(5)
n_4.next = n_5

m_1 = Node(6)
m_2 = Node(7)
m_1.next = m_2
m_3 = Node(8)
m_2.next = m_3


new_L = combine_singly_linked_lists(n_1, m_1)
while new_L:
    print(new_L.data)
    new_L = new_L.next


