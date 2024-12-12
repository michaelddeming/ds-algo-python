"""Give a big-Oh characterization, in terms of n, of the running time of the
example1 function shown in Code Fragment 3.10."""

def example1(S):

    n = len(S) # contant time
    total = 0 # constant time
    for j in range(n): # linear time
            total += S[j] # consant time
    return total #return, constant time

# example1 = O(n)



