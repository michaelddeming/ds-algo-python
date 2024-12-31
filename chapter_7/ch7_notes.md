# Chapter 7: Linked Lists

---

## Definitions:

1. Traversing: Starting at the head of the linked list, reaching the tail where the next reference is None. 
2. Link/Pointer: 

---

## 7.1: Singly Linked Lists

- Singly Linked List: is a collection of nodes that collectively form a linear sequence. Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node in the list. 

    - Examples:
    1. 
    2. 
    3. 

    - Head: the first node in the linked list.
    - Tail: the last node in the linked list.

---

## 7.2: Circularly Linked Lists

- Circularly Linked List: The tail of the Linked List uses it's next reference to point back to the head of the list, rather than None in a singularly linked list. 

    - Examples:
    1. Order of train spots in the Chicago loop.
    2. Players taking turns in a game. 

    - CLL has not "start" or "end", due to the looping effect of the tail ref pointing back to head. 
        - We must maintain a ```current```variable to house the location or node we are currently at. 
        - ```current = current.next```

- Round-Robin Schedulers: Typically in the form of a Queue ADT, elements are dequeued and a shared action is perform on said element, element is then enqueued back into the Queue.

---

## 7.3: Doubly Linked Lists

- Doubly Linked List: A linked list in which each node keeps an explicit reference to the node before it  and a reference to the node after it. 

    - Examples:
    1.
    2. 

    -  DLL can keep a sentinel ```header``` node at the beginning of the list, and a ```trailer```node at the end of the list. 
        - These are "dummy" nodes that act as guards and do not store elements of the primary sequence. 

---

## 7.4: The Positional List ADT

- 




    





