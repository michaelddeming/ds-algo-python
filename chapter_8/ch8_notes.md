# Chapter 8: Trees

---

## 8.1: General Trees

- Trees: A tree is a way to organize data in a structure with nodes connected by lines, called edges. It starts from one main point, called the root, and branches out to other points (nodes). Each node can have more nodes connected to it. Trees are used to represent things that have a starting point and branches, like a family tree or folder system. 

- Tree Formal Def:  a tree T as a set of nodes storing elements such that the nodes have a parent-child relationship that satisfies the following properties:
    - If T is nonempty, it has a special node, called the root of T , that has no parent.
    - Each node v of T different from the root has a unique parent node w; every node with parent w is a child of w. Note that according to our definition, a tree.

- Siblings: Two nodes that are children of the same parent.
- External: A node that has no children aka *"leaves"*.
- Internal: A node that has 1 or more children.
- Ancestor/Descendant: node u is an ancestor of a node v if u = v or u is an *ancestor* of the parent of v. Conversely, we say that a node v is a *descendant* of a node u if u is an ancestor of v.
    - A node can be an ancestor of itself given this definition. 
- Edges: The "connection" or "pointer" between a parent node and it's child or vice versa.
- Path: A sequence of nodes that any two consecutive nodes in the sequence form an edge.   

- Ordered Trees: A tree is *ordered* if there is a meaningful linear order among the children of each node; first child, second child, etc. Visualized in left to right order. 
    - Example: A book would be the root, it's Preface is the first child, Chapter 1 is the second child, and so-on. 

