"""Python’s random module includes a function choice(data) that returns a
random element from a non-empty sequence. The random module in-
cludes a more basic function randrange, with parameterization similar to
the built-in range function, that return a random choice from the given
range. Using only the randrange function, implement your own version
of the choice function."""

import random


def choice_recreated(data):

    random_index = random.randrange(len(data))
    return data[random_index]


dummy_list = [1, 6, 4, 9, 3, 2]

print(choice_recreated(dummy_list))
