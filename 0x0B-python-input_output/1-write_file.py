#!/usr/bin/python3
"""this module writes stufdf"""


def write_file(filename="", text=""):
    """this function writes stuff tooo"""
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
