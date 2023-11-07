#!/usr/bin/python3
"""this module wirtes json to text fiile"""

import json


def save_to_json_file(my_obj, filename):
    """this function writes data on the file"""
    with open(filename, 'w', encoding='utf-8') as t_file:
        json_str = json.dumps(my_obj)
        t_file.write(json_str)
