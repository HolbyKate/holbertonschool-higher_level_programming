#!/usr/bin/python3
"""Task: 9-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self._width = width
        """Define positive integers, validated by integer_validator"""
        self.integer_validator("height", height)
        self._height = height

    def area(self):
        """Return the area of the rectangle"""
        return self._width * self._height

    def _str_(self):
        """
        print() should print, and str() should return, the following rectangle
        description: [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self._width}/{self._height}"
