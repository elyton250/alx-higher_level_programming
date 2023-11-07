#!/usr/bin/python3
"""this file reads from JSON"""


def load_from_json_file(filename):
    """this function reads from a file"""
    with open(filename, 'r', encodin='utf-8') as j_file:
        json_str = j_file.read()
        return json.loads(json_str)
