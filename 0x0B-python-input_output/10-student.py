#!/usr/bin/python3

"""This module defines a class Student."""


class Student:
    """This class represents a student."""
    def __init__(self, first_name, last_name, age):
        """This function initializes a Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This function returns a dictionary representation."""
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
