"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""


def minmax(data):

    max_value, min_value = data[0], data[0]
    for value in data:
        if value > max_value:
            max_value = value
        elif value < min_value:
            min_value = value

    return min_value, max_value


data = [1, 5, 4, 6, 25, 8]

print(minmax(data))
