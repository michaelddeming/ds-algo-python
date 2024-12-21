"""Describe a recursive algorithm to compute the integer part of the base-two
logarithm of n using only addition and integer division."""

def log(n):

    # 2^x = n, solve for x

    if n == 1:
        return 0
    
    return log(n//2) + 1

print(log(16))

# O(logn)




