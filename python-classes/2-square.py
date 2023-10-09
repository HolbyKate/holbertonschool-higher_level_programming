#!/usr/bin/python3
"""
Module 1-square
Defines class Square with private instance
"""


class Square:
    """Write a empty class"""
    def __init__(self, size=0):
        self.__size = size
        """define private instance attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """define square"""
