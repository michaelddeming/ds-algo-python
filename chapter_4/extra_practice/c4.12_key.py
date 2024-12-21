"""Give a recursive algorithm to compute the product of two positive integers,
m and n, using only addition and subtraction."""

def product(m: int, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return m
    else:
       return m + product(m, n-1)
    
print(product(100, 100))