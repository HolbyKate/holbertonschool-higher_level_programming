#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """Check if both a and b are either integers or floats"""

    if type(a) is not int and type(a)is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b)is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    """Return the addition of a and b"""
    return (a + b)
