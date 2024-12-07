"""What are some potential efficiency disadvantages of having very shallow
inheritance trees, that is, a large set of classes, A, B, C, and so on, such
that all of these classes extend a single class, Z?"""

# assuming that being close in relation (child) to the base (parent) class, methods and/or attributes could cross-over in excess. 
    # a child class may only differ from the parent by a small amount, causing excess code. You could apply those "attributes/methods" to the parent as optional. 

# adding additional functionality to the parent class could be difficult if many child classes are impacted.