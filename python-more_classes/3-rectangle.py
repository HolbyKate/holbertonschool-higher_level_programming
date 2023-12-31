#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """Define a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """define instance method that returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """ if width or height is equal to 0, perimeter is equal to 0"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ("")
        for i in range(self.height):
            for j in range(self.width):
                rectangle += "#"
            if i < self.height - 1:
                rectangle += "\n"
        return rectangle
