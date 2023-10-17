#!/usr/bin/python3
"""Task: 2-is_same_class.py"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
