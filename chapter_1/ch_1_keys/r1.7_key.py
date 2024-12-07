"""Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function."""

def sum_sq_odd_range(n: int):
    return sum(value**2 for value in range(1,n) if n > 0 and value % 2 != 0)

print(sum_sq_odd_range(100))
