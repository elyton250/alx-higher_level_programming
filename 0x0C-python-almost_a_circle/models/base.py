#!/usr/bin/python3
"""this module is the base of the classes"""

import json


class Base:
    """Base class for all other classes in the project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance with a given id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to json string"""
        if list_dictionaries is None:
            return "[]"
        else:
            json_data = json.dumps(list_dictionaries)
            return json_data

    @classmethod
    def save_to_file(cls, list_objs):
        """it writes a json string represenattion of objects"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as j_file:
            if list_objs is None:
                empty = []
                j_file.write("[]")
            else:
                json_string = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
                j_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns a list of json rep"""
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """this sets attributes"""
