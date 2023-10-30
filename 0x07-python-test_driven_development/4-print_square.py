#!/usr/bin/python3
"""this module prints squares"""


def print_square(size):
    """This function accept the size of the square and prints it"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    count = size
    while count > 0:
        print("#" * size)
        count = count - 1
