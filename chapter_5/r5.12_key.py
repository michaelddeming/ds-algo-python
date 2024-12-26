"""Describe how the built-in sum function can be combined with Python's
comprehension syntax to compute the sum of all numbers in an n x n data
set, represented as a list of lists."""

data = [[22, 18, 709, 5, 33], [45, 32, 830, 120, 750], [4, 880, 45, 66, 61]]


def sum_matrix(matrix):
    count = 0

    for l in matrix:
        count += sum(l)
    return count
            



def sum_matrix_2(matrix):

    count = sum(sum(l) for l in matrix)
    return count

print(sum_matrix_2(data))