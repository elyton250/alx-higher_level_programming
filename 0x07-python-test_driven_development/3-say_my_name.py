#!/usr/bin/python3
"""this module prints the first and last name of clients"""


def say_my_name(first_name, last_name=""):
    """This fuunctions accept 2 strings
    and prints them on the sma line separated with space"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
