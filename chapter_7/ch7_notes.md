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

- Positional List ADT: a list-like data structure that allows elements to be accessed, inserted, or removed based on their "position" while maintaining relationships between adjacent elements/nodes.

    - Examples:
    1. Cursor in a text document.
    2. Cutting in line or queue.

    - Indexs vs Positions: Positions are abstract markers or references to elements in the list. They do not correspond to fixed numeric values. Indicies are number and correspond to teh absolute position of an element. 
        - Position --> bookmark in a book
        - Index --> page number of a book

    - Position instances are simple objects that support the following method:
        1. p.element(): Return the element stored at position p. 

    - A Positional List, L, supports the following methods:
        1. L.first(): Return the position of the first element of L, or None if L is empty.
        2. L.last(): Return the position of the last element of L, or None if L is empty.
        3. L.before(p): Return the position of L immediately before position p, or None
        if p is the first position.
        4. L.after(p): Return the position of L immediately after position p, or None if
        p is the last position.
        5. L.is_empty(): Return True if list L does not contain any elements.
        6. len(L): Return the number of elements in the list.
        7. iter(L): Return a forward iterator for the elements of the list. See Sec-
        tion 1.8 for discussion of iterators in Python.
    
    - The positional list ADT also includes the following update methods:
        1. L.add_first(e): Insert a new element e at the front of L, returning the      position of the new element.
        2. L.add_last(e): Insert a new element e at the back of L, returning the position
        of the new element.
        3. L.add before(p, e): Insert a new element e just before position p in L, returning
        the position of the new element.
        4. L.add_after(p, e): Insert a new element e just after position p in L, returning
        the position of the new element.
        5. L.replace(p, e): Replace the element at position p with element e, returning
        the element formerly at position p.
        6. L.delete(p): Remove and return the element at position p in L, invalidat-
        ing the position.



---

## 7.5: Sorting a Positional List.

- 




    





