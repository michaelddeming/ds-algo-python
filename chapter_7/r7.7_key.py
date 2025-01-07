"""Our CircularQueue class of Section 7.2.2 provides a rotate() method that has semantics equivalent to Q.enqueue(Q.dequeue()), for a nonempty queue. Implement such a method for the LinkedQueue class of Section 7.1.2 without the creation of any new nodes."""

def rotate(self):
    
    # if self.is_empty():
    #     raise Empty("Queue is empty") --> already being called in thed dequeue method. 
    
    
    removed = self.dequeue()
    self.enqueue(removed)

    


    

    

    

    