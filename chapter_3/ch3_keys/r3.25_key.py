"""Give a big-Oh characterization, in terms of n, of the running time of the
example3 function shown in Code Fragment 3.10."""

def example3(S):
    n = len(S) #costant time
    total = 0 #constant time
    for j in range(n): # linear
        for k in range(1+j): # nested linear
            total += S[k] # constant
        return total # constant
    
# example3 = O(n^2) 