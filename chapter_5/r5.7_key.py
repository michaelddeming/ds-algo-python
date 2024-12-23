"""Let A be an array of size n ≥ 2 containing integers from 1 to n - 1, inclu-
sive, with exactly one repeated. Describe a fast algorithm for finding the
integer in A that is repeated."""

# n = 6

A_1 = [1, 2, 3, 4, 5, 5]

# 1. Assuming that the array is UNORDERED:
# Iterate over every value in the array, saving unique values in a set (no dups allowed), comparing next value with values in set, returning a duplicate if found.

    # O(n) * O(1) --> O(n)

def dup_found(A):

    uniques = set()

    if len(A) > 1:
        for val in A:
            if val in uniques:
                return val
            uniques.add(val)
    return None
            
print(dup_found(A_1))

# 2. Assuming that the array is ORDERED:
# Iterate over values in the array, saving index values as well, and checkind adjacent value/index is equal, if so return value, else continue iterating.