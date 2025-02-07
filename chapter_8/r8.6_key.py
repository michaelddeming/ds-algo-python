"""Let T be an n-node binary tree that may be improper. Describe how to represent T by means of a proper binary tree T' with O(n) nodes."""

# An improper Binary Tree is one where nodes have just one child. In a proper Binary Tree, nodes have either 0 or 2 children, thus keeping the "binary" feature. 

# You could recursively move through the improper Binary Tree and detect the number of children at each node. If a node only has one child, insert a dummy node as the missing child to make it a proper binary tree. Since each node is visited once, and at most one dummy node is added per node, maintaining an O(n) time complexity.  