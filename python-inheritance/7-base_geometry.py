#!/usr/bin/python3
"""Task: 7-base_geometry.py"""


class BaseGeometry():
    """Create an empty class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
