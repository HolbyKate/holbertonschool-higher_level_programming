#!/usr/bin/python3
"""Task: 8-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self._width = width
        self._height = height
        """Define positive integers, validated by integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
