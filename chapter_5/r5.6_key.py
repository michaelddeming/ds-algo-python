"""Our implementation of insert for the DynamicArray class, as given in
Code Fragment 5.5, has the following inefficiency. In the case when a re-
size occurs, the resize operation takes time to copy all the elements from
an old array to a new array, and then the subsequent loop in the body of
insert shifts many of those elements. Give an improved implementation
of the insert method, so that, in the case of a resize, the elements are
shifted into their final position during that operation, thereby avoiding the
subsequent shifting."""

# j = -5 -4 -3 -2 -1 --> reverse index

# i =  0  1  2  3  4 --> forward index

# l = [5, 3, 6, 8, 2] --> n = len(l) = 5

# insert(k=2)

def insert(self, k, value):

    if self._n == self._capacity:
        new_array = [None] * (2 * self._capacity)

        for i in range(k):
            new_array[i] = self._A[i]

        new_array[k] = value

        for i in range(k, self._n):
            new_array[i+1] = self._A[i]

        self._A = new_array

        self._capacity = 2 * self._capacity


    else:
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
    self._n += 1