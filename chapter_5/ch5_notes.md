# Chapter 5: Array-Based Sequences

### Definitions 
- list:
- tuple:
- str:
- bit: The smallest unit of data, representing a binary value (0 or 1). 
- byte: A group of 8 bits, which often represents a single character or a small amount of data.
- memory address: A unique identifier for a location in a computer’s memory where data is stored. 
- RAM: Random Access Memory
- Array: A group of related variables, stored in continously in the computer's memory. 

---

## 5.1: Python's Sequence Types

---

## 5.2: Low-Level Arrays

- Low Level Arrays: 
    1. Fixed Size: The size of the array is typically defined when it is created and cannot be changed dynamically.

    2. Contiguous Memory Allocation: Elements are stored in consecutive memory locations, allowing for fast access using an index.

    3. Homogenous Elements: All elements in the array must be of the same data type, such as integers or characters.

    4. Manual Memory Management: In languages like C or C++, developers must manually allocate and deallocate memory for arrays.

    5. Efficient Access: Because of their contiguous memory layout, accessing elements via an index is very fast (constant time, O(1)).

    6. Lack of Build-In Safety: Many low-level arrays do not perform bounds checking, meaning accessing elements outside the allocated range can lead to undefined behavior or memory corruption.

- Bytes can be accessed by a computer through its RAM (Random Access Memory) via its memory address (byte #8675309). An individual byte  of memory can be stored or accessed in O(1) time. 

- Text characters, using the Unicode character system, take up 16 bits or 2 bytes of memory per character. 
    - Example: "SAMPLE" --> 6 character * 2 bytes each = 12 bytes total for the string array "SAMPLE" in the systems memory. 

- Compact Arrays: a way to organize data in a memory-efficient manner by using only the minimum amount of space needed to store the values. Instead of leaving gaps or unused memory, it keeps the data tightly packed together.

---

## 5.3: Dynamic Arrays and Amortization

- Dynamic Array: when a list is created in Python, it allocates a “dynamic array” in the system’s memory, reserving extra space to allow the list to grow as elements are appended. Once this extra space is fully used, Python requests the system to allocate a larger dynamic array. The existing elements are copied into the new array, and the old one is discarded, allowing the list to continue growing seamlessly.
    - Lists house references to the objects inside. The physical memory of the individual objects is not applied to the list's memory size. The objects are house elsewhere in memory. 

- Amortization:

Geometric Increase in Capacity:

---

## 5.4: Efficiency of Python's Sequence Types

- List & Tuple Classes:
    - Tuples are typically more memory efficient because they are immutable (can not be changed). 

Methods:
- .pop() removes the last element from a list.
- .pop(k) removes the element at index k, where k < n, shifts all remaining rightward elements to the left to fill the gap.
    - O(n-k)
    - pop(0) --> Ω(n) for the base case because you have to pass over all values starting from the end via .pop() definition. 

- .remove(val) removes the first occurance of val found in the array.
    - Raises ValueError if the provided val in not found. 
    - Ω(n) for the best case case because you interate up to the val and shift all rightward values to the left to fill the gap.

- .extend(other_list) concatenates the other_list provided to the end of the list the method is called on.
    - For many "append" operations, the .extend method is preferred over a for loop due to pre-determining the new array size in one .extend call with a known "other_list" size rather than potentially resize many times.

---

## 5.4: Efficiency of Python's Sequence Types














