"""Implement the neg method for the Vector class of Section 2.3.3, so
that the expression -v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v."""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self. coords = [0] * d


def __neg__(self):
    new_negative_vector = Vector(len(self))
 
    
    for index in range(len(self)):
        new_negative_vector[index] = self[index] * -1
    
    return new_negative_vector


