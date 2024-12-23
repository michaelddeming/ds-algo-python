"""Our DynamicArray class, as given in Code Fragment 5.3, does not support
use of negative indices with __getitem__. Update that method to better
match the semantics of a Python list."""


# i = -5 -4 -3 -2 -1
# l = [4, 2, 5, 1, 6]

def __getitem__(self, k):

    if 0 <= k < self._n:
        return self._A[k]
    elif -(self._n) <= k <= -1:
        return self._A[k + self._n]
    
