#!/usr/bin/python3
"""
Contains method that divides all elements of a matrix and returns new matrix
Requires same size lists of ints or floats, and max two decimal places
"""


def say_my_name(first_name, last_name=""):

    msg = "say_my_name() missing 1 required positional argument: 'first_name'"

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if len(first_name) == 0 and len(last_name) == 0:
        raise TypeError(msg)
    print(f"My name is {first_name} {last_name}")
