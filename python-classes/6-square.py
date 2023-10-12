#!/usr/bin/python3
"""
Module 4-square
Defines class Square based on 3-square.py
"""


class Square:
    """Write a empty class"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """define private instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """define square"""

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with error checking"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            if len(value) != 2 or not all(isinstance(x, int) and x >= 0):
                for x in value:
                    raise TypeError("position must be a"
                                    "tuple of 2 positive integers")
                self.__position = value

    def area(self):
        """define instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """This def prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
