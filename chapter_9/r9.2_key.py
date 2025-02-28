"""Suppose you label each position p of a binary tree T with a key equal to its preorder rank. Under what circumstances is T a heap?"""

# the circumstance where the tree is a heap after labeling nodes with their preorder ranks is when the tree’s nodes are sorted in ascending order for a min-heap or descending order for a max-heap.

# 	•	In a min-heap, the smallest elements (with smaller preorder ranks) would naturally come first in the traversal, and they would be placed at the top of the tree or as left children, maintaining the heap’s requirement that parents must be smaller than their children.
#   •	In a max-heap, the reverse would occur. The largest elements would appear first in the preorder traversal and end up as the root, maintaining the heap property with each parent node being larger than its children.

