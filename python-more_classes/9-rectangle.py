#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """Define a rectangle"""
    number_of_instances = 0
    print_symbol = "#"
    """insert public class attribute"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using eval()"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)

    def __del__(self):
        """Delete a rectangle"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
