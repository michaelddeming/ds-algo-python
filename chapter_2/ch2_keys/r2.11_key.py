"""In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10,-2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10,-2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector."""


# You can either implement an entire new __radd__ method to catch when the addition order changes. 

# OR because __add__ already checks if len(self) != len(other), we can just convert other into a Vector object and successfully perform the addition of 2 Vector object together. 

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self. coords = [0] * d

    # ... etc. 

def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):
        raise ValueError("dimensions must agree")
    if isinstance(other, Vector) == False:
        other = Vector(other)
    result = Vector(len(self))

    for index in range(len(self)):
        result[index] = self[index] + other[index]
    return result

    






