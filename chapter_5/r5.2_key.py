"""In Code Fragment 5.1, we perform an experiment to compare the length of
a Python list to its underlying memory usage. Determining the sequence
of array sizes requires a manual inspection of the output of that program.
Redesign the experiment so that the program outputs only those values of
k at which the existing capacity is exhausted. For example, on a system
consistent with the results of Code Fragment 5.2, your program should
output that the sequence of array capacities are 0, 4, 8, 16, 25, . . . ."""

import sys



def get_size_change(n):
    data = []
    B_list = []
    B = None #56
    for k in range(0, n+1):
        a = len(data)
        b = sys.getsizeof(data)
        if B != b:
            B_list.append(b)
            B = b
            data.append(None)
        data.append(None)
    return B_list     


print(get_size_change(26))