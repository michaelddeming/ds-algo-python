"""What values are returned during the following sequence of queue operations, if executed on an initially empty queue? enqueue(5), enqueue(3),
dequeue(), enqueue(2), enqueue(8), dequeue(), dequeue(), enqueue(9), enqueue(1), dequeue(), enqueue(7), enqueue(6), dequeue(), dequeue(), enqueue(4), dequeue(), dequeue()."""


# using the "circular array" queue concept

# Q = [None, None, None, None, None, None, None, None, None, None] FIFO

# enqueue(5)
# Q = [5, None, None, None, None, None, None, None, None, None] FIFO

# enqueue(3)
# Q = [5, 3, None, None, None, None, None, None, None, None] FIFO

# dequeue()
# Q = [None, 3, None, None, None, None, None, None, None, None] FIFO

# enqueue(2)
# Q = [None, 3, 2, None, None, None, None, None, None, None] FIFO

# enqueue(8)
# Q = [None, 3, 2, 8, None, None, None, None, None, None] FIFO

# dequeue()
# Q = [None, None, 2, 8, None, None, None, None, None, None] FIFO

# dequeue()
# Q = [None, None, None, 8, None, None, None, None, None, None] FIFO

# enqueue(9)
# Q = [None, None, None, 8, 9, None, None, None, None, None] FIFO

# enqueue(1)
# Q = [None, None, None, 8, 9, 1, None, None, None, None] FIFO

# dequeue()
# Q = [None, None, None, None, 9, 1, None, None, None, None] FIFO

# enqueue(7)
# Q = [None, None, None, None, 9, 1, 7, None, None, None] FIFO

# enqueue(6)
# Q = [None, None, None, None, 9, 1, 7, 6, None, None] FIFO

# dequeue()
# Q = [None, None, None, None, None, 1, 7, 6, None, None] FIFO

# dequeue()
# Q = [None, None, None, None, None, None, 7, 6, None, None] FIFO

# enqueue(4)
# Q = [None, None, None, None, None, None, 7, 6, 4, None] FIFO

# dequeue()
# Q = [None, None, None, None, None, None, None, 6, 4, None] FIFO

# dequeue()
# Q = [None, None, None, None, None, None, None, None, 4, None] FIFO