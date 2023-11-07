#!/usr/bin/python3

"""this module appends stuff"""


def append_write(filename="", text=""):
    """this function apppends stuff"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
