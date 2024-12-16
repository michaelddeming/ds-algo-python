# Chapter 4: Recursion

### Definitions 
- Recursion: a technique by which a function makes one or more calls to itself
during execution, or by which a data structure relies upon smaller instances of the very same type of structure in its representation.
- Permutations: the number of ways in which n distinct items can be arranged into a sequence
- Base Cases: conditions under which the recursion stops. They serve as the simplest instances of a problem that can be solved directly without further recursion.
- Recursive Cases: the part where the function calls itself with a smaller or simpler version of the original problem.
- Fractal: a shape that has a self-recursive structure at various levels of magnification.
- 

---

## 4.1 & 4.2: Illustrative Examples and Analyzing Recursive Algorithms

1. **Factorial Function**: (commonly denoted as n!) is a classic mathematical
function that has a natural recursive definition.

 
    - **Recursive Definition**: 

        n! = {1 , if n = 0} or {n * (n-1)! , if n >= 1}

        ```python
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        ```
        
        ![A recursion trace for the call factorial(5)](/chapter_4/recursion_trace.jpg)

2. **English Ruler**: a recursive pattern that is a simple example of a 
structure.









3. **Binary Search**: one of the most important computer algorithms. It allows
us to efficiently locate a desired value in a data set with upwards of billions of entries.

    - Sorted lists/datasets
    - Sequential Search: Using a loop to examine every element in a dataset, until either finding the target element or exhausting the dataset.
    - Binary Search: Binary search is a method to find an item in a sorted list. It works by dividing the list in half repeatedly:
	    1.  Start with two pointers, low (beginning of the list, index 0) and high (end of the list, index n-1).
	    2.  Find the middle index: mid = (low + high) // 2.
	    3.  Compare the target value with the value at the middle index:
	        •	If the target is larger, search the right half of the list (low = mid + 1).
	        •	If the target is smaller, search the left half (high = mid - 1).
	    4.  Repeat until you find the target or the list is empty.

        ```python
            def binary_search(data, target, low, high):
                """Return True if target is found in indicated portion of a Python list.
                
                The search only considers the portion from data[low] to data[high] inclusive.
                """
                if low > high:
                    return False  # Interval is empty; no match
                else:
                    mid = (low + high) // 2
                    if target == data[mid]:  # Found a match
                        return True
                    elif target < data[mid]:
                        # Recur on the portion left of the middle
                        return binary_search(data, target, low, mid - 1)
                    else:
                        # Recur on the portion right of the middle
                        return binary_search(data, target, mid + 1, high)
        ```

4. **File System**: A recursive structure in which directories can be nested arbitrarily deeply within other directories.

---

## 4.3: Recursion Run Amok

- **Infinite Recursion**: Occurs when a recursive call makes another recursive call without ever reaching a base case.
    - Python has a built-in safety feature that caps the depth of recursion at approximately 1000. If exceeded, it raises a `RuntimeError`.
    - Python's `sys` module allows dynamic reconfiguration of the recursion limit using the functions `getrecursionlimit` and `setrecursionlimit`.
    - **Example**:

      ```python
      import sys
      old = sys.getrecursionlimit()  # perhaps 1000 is typical
      sys.setrecursionlimit(1000000)  # change to allow 1 million nested calls
      ```

---

## 4.4: Further Examples of Recursion

1. Linear Recursion: recursive call starts at most one other. 
2. Binary Recursion: recursive call may start two others.
3. Multiple Recursion: recursive call may start three or more others.

---

## 4.4: Further Examples of Recursion

---

## 4.5: Designing Recursive Algorithms

1. Test for base cases:
2. Recur: 
    - Parameterizing a Recursion:

---

## 4.6: Eliminating Tail Recursion

- **Tail Recursion**: the recursive call is the last operation in the function. In other words, the function returns the result of the recursive call directly, without any additional computation after it.



