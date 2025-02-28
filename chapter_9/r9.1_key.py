"""How long would it take to remove the ⌈logn⌉ smallest elements from a
heap that contains n entries, using the remove min operation?"""

# 1. The removal of the smallest (root) element in the heap would have constant time, O(1). 

# 2. The swap of the last element to the root position would also be constant, O(1). 

# 3. However during the "heapify" function, the root replacement tuple pair will cascade downward via the down-heap bubbling, swapping positions in the worst-case time, O(log(n)) for having to traverse the half the tree to it's furthest depth. 

# 4. Due to the question wanting to remove the ⌈logn⌉ smallest elements, the total runningtime of the operation would take O(log(n)^2) or O(log(n)*log(n)).