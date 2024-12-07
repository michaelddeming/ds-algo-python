"""Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v."""



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
    
    def __rmul__(self, factor: int | float):
        new_vector = Vector(len(self))

        for index in range(len(self)):
            new_vector[index] = factor * self[index]
        return new_vector