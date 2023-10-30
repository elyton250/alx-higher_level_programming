#!/usr/bin/python3
""" this module adds 2 intgeers"""


def add_integer(a, b=98):
    """ this functions take in 2 arguments transforms them into integrs and
    and return their sum"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
