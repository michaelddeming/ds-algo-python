"""Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors, that is, ∑d,i=1 ui· vi."""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d

    # ... etc. 

    def __mul__(self, other):

        if len(self) != len(other):
            raise ValueError("dimension need to be equal")
        
        dot_product = 0

        for index in range(len(self)):
            dot_product += self[index] * other[index]

        return dot_product
        
        
        
        
        
            


