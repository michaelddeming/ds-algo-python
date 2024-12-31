"""Give a simple adapter that implements our queue ADT while using a collections.deque instance for storage."""

from collections import deque

class Queue():

    def __init__(self):
        self._data = deque()

    def enqueue(self, element):
        self._data.append(element)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._data.popleft()
    
    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0
    
    def size(self):

        return len(self._data)
    




    