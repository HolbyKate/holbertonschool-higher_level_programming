#!/usr/bin/python3
"""Task: 1-my_list"""


class Mylist(list):
   """
    Extends the built-in list class with additional functionality.

    This class inherits from the built-in list class and adds a custom method
    called `print_sorted` to print the elements of the list in sorted order.

    Attributes:
        Inherits all attributes and methods from the built-in list class.

    Methods:
        print_sorted(self):
            Print the elements of the list in sorted order.

            This method sorts the elements of the list in ascending order and
            prints them.

    Parameters:
        None

    Returns:
        None
    """


def print_sorted(self):
    """Prints list in ascending sort"""
    print(sorted(self))
