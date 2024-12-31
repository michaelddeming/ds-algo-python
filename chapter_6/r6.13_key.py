"""Suppose you have a deque D containing the numbers (1,2,3,4,5,6,7,8),
in this order. Suppose further that you have an initially empty queue Q.
Give a code fragment that uses only D and Q (and no other variables) and
results in D storing the elements in the order (1,2,3,5,4,6,7,8)."""

from collections import deque

D_1 = [1, 2, 3, 4, 5, 6, 7, 8]

# Queues: First In First Out (FIFO)
    # when using the Python deque() class as an adapter class for a queue, only 
    # Q.append() and Q.popleft() are permitted.

def swap(D):

    Q = deque()

    D = deque(D)

    while D[0] != 4:
        Q.append(D.popleft())
        D.append(Q.popleft())
    
    while D[0] != 5:
        Q.append(D.popleft())
    
    D.append(D.popleft())
    D.append(Q.popleft())

    while D[0] != 1:
        Q.append(D.popleft())
        D.append(Q.popleft())

    return D

        


print(swap(D_1))
