#!/usr/bin/python3
"""Module rectangle.py"""

from models.base import Base


class Rectangle(Base):
    """the class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance.
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int, optional): The x-coordinate of the rectangle. Defaults to 0
            y (int, optional): The y-coordinate of the rectangle. Defaults to 0
            id (int, optional): The ID of the rectangle. Defaults to None
        """
    super().__init__(id)
    self.__width = width
    self.__height = height
    self.__x = x
    self.__y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value