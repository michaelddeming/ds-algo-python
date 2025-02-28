"""The min method for the UnsortedPriorityQueue class executes in O(n) time, as analyzed in Table 9.2. Give a simple modification to the class so that min runs in O(1) time. Explain any necessary modifications to other methods of the class."""

# We can modify the UnsortedPriorityQueue class by keeping a minimum variable/container within the class overall and evaluating as elements are added to the queue. This way we no longer have to iterate over n and during the _find_min() function evaluating smallest for every element in n. 

# This would completely remove the _find_min() function and the min() function would return the current p.element within the "smallest" class instance variable. 

# The remove_min() function would need to pop the current class minimum element and scan over n to find the second lowest element, now the new minimum. 