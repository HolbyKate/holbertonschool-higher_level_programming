#!/usr/bin/python3
"""Task: 9-student.py"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Instantiation with public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance"""
        return self.__dict__
