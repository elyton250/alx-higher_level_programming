#!/usr/bin/python3

"""this module reads a file """


def read_file(filename=""):

    """this function reads a file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read(), end='')
