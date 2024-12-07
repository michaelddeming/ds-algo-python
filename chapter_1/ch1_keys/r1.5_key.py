"""Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function."""

def sum_sq_range(n: int):
    return sum(value*value for value in range(1,n) if n > 0)

# print(sum_sq_range(100))