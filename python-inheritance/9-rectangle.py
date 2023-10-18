#!/usr/bin/python3
"""Task: 9-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        """Define positive integers, validated by integer_validator"""
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        print() should print, and str() should return, the following rectangle
        description: [Rectangle] <width>/<height>
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
