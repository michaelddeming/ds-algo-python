"""Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v."""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self. coords = [0] * d

    # ... etc. 

                                # type hint support with Python 3.10
    def __mul__(self, factor: int | float):
        new_vector = Vector(len(self))

        for index in range(len(self)):
            new_vector[index] = self[index] * factor
        return new_vector