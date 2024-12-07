"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""

def sum_sq_odd_range(n: int):
    if n > 0:
        count = 0 
        for value in range(1, n):
            if value % 2 != 0:
                count += (value**2)
        return count

print(sum_sq_odd_range(100))
