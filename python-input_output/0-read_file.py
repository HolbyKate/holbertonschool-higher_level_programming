#!/usr/bin/python3
"""Task: 0-read_file.py"""


def read_file(filename=""):
    """Function that read a text file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
