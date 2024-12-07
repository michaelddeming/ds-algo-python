""" The Vector class of Section 2.3.3 provides a constructor that takes an in-
teger d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
nates <4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it pro-
duces a vector with coordinates based on that sequence."""

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d_or_values):
        """Create d-dimensional vector of zeros."""
        if isinstance(d_or_values , int):
            self._coords = [0] * d_or_values
        elif isinstance(d_or_values, (tuple, list)):
            self._coords = list(d_or_values)   
        else:
            raise ValueError("Vector construct in incorrect format")
                


