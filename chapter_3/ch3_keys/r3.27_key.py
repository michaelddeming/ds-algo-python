"""Give a big-Oh characterization, in terms of n, of the running time of the
example5 function shown in Code Fragment 3.10."""

def example5(A, B): 

    n = len(A) # constant
    count = 0 # constant
    for i in range(n): # linear
        total = 0 # constant
        for j in range(n): # nested linear
            for k in range(1+j): # nested linear
                total += A[k] # constant
            if B[i] == total: # constant
                count += 1 # constant
    return count # constant

# example5 = O(n^3)
