#!/usr/bin/python3
"""this file reads from JSON"""

import json


def load_from_json_file(filename):
    """this function reads from a file"""
    with open(filename, 'r', encoding='utf-8') as j_file:
        return json.load(j_file)
