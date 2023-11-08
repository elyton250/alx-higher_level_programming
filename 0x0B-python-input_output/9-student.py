#!/usr/bin/python3

"""This module defines a class Student."""


class Student:
    """This class represents a student."""
    def __init__(self, first_name, last_name, age):
        """This function initializes a Student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function returns a dictionary representation."""
        return self.__dict__
