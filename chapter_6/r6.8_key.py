"""Suppose an initially empty queue Q has executed a total of 32 enqueue operations, 10 first operations, and 15 dequeue operations, 5 of which
raised Empty errors that were caught and ignored. What is the current
size of Q?"""

# enqueue 32 elements into the Q

# 10 first operations, references to the first value on the queue, does not remove the value

# 15 dequeue operations, 5 resulted in empty errors --> 15 - 5 = 10 successful dequeue operations.

# 32 enqueue - 10 dequeue operations = 22 elements in the Q 

# Q._size = 22





