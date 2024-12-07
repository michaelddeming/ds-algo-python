"""Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256]."""


recreated_list = [value for value in range(1,256+1) if 256 % value == 0]
print(recreated_list)