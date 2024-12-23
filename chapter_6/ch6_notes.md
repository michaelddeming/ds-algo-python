# Chapter 6: Stacks, Queues, and Deques (Decks)

### Definitions

---

## 6.1: Stacks

- Stack: a collection of objects that are inserted and removed according to the last-in, first-out (LIFO) principle.

    - Examples:
        1. Internet Web Browers "back" button.
        2. Text editors or the ctrl (cmd) + z functionality to "undo" changes.

    - Stacks are Abstract Data Types (ADTs), an instance of S supports:
        1. S.push(e): Add element e to the top of the stack S (S.append(e) in Python).
        2. S.pop(): Remove and return the tio element from the stack S; an error occurs if the stack is empty. 
        3. S.top(): Returns a REFERENCE to the top element of the stack S, without removing it from the stack; an error occurs if the stack is empty. (S[-1] in Python)
        4. S.is_empty(): Return True is stack S does not contain any elements. (len(S) == 0 in Python)
        5. len(S): Returns the number of elements in stack S; in Python, we implement this with the special ```__len__```. 

    - Stack Running Times:
        - .top(), .is_empty(), and len() use constant time in the worst case, O(1).
        - .push(), .pop() are amoritied O(1) time because of the possible dynamic array re-sizing underneath which takes O(n). 
        - Space usage for a stack is O(n).


