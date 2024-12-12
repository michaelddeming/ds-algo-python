"""Give a big-Oh characterization, in terms of n, of the running time of the
example4 function shown in Code Fragment 3.10."""

def example4(S):
    n = len(S)
    prefix = 0 #constant
    total = 0 #constant
    for j in range(n): # liner
        prefix += S[j] # consant
        total += prefix # constant
    return total # constant

# example4 = O(n)