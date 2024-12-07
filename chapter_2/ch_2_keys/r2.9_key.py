"""Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u-v returns a new vector instance representing the
difference between two vectors."""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self. coords = [0] * d



def __sub__(self, other):
    """Return difference of two vectors."""
    if len(self) != len(other):
        raise ValueError('dimensions must agree') # vector self & other must have the same length to be operated on
    
    result = Vector(len(self)) # creates a vector with 0's for len(self)

    # < 0, 0, 0, 0 >

    for val in range(len(self)):
        result[val] = self[val] - other[val]
    return result

   
    