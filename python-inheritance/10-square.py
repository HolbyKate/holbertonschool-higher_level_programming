#!/usr/bin/python3
"""Task: 10-rectangle.py"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Instantiation with size"""
    def __init__(self, size):
        """Initializes private and positive size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
