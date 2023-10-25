#!/usr/bin/python3
"""Module base.py"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list dict"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json strings of all instances into file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        The filename is constructed using the class name:
          "<Class name>.json" (e.g., "Rectangle.json").
        If the file doesn’t exist, an empty list is returned.

        Returns:
            list: A list of instances of the current class.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                data = Base.from_json_string(file.read())
                instances = []
                for item in data:
                    instances.append(cls.create(**item))
                return instances
        except FileNotFoundError:
            return []
