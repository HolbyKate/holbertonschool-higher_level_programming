#!/usr/bin/python3
"""Task: 2-append_write.py"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)
