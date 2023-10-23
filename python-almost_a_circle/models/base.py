#!/usr/bin/python3
"""Module base.py"""


class Base:
    """Write a class with a private class attribute and class construction"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
