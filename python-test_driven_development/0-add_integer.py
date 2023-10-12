#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """Check if both a and b are either integers or floats"""
    if a is not isinstance(int, float):
        raise TypeError("a must be an integer")
    elif b is not isinstance(int, float):
        raise TypeError("b must be an integer")
    else:
        """Return the addition of a and b"""
        return (a + b)
