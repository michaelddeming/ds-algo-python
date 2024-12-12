"""Give a big-Oh characterization, in terms of n, of the running time of the
example2 function shown in Code Fragment 3.10."""

def example2(S):
    """Return the sum of the elements with even index in sequence S."""
    n = len(S) # contant time
    total = 0 #constant time
    for j in range(0, n, 2): # linear time
        total += S[j] #constant time
    return total #costant time