#!/usr/bin/python3
"""this module retunz the dixt representation od data structures"""


def class_to_json(obj):
    """this functions return dict description"""
    return obj.__dict__
