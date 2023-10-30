#!/usr/bin/python3
"""This module creates sentences from a paragraph"""


def text_indentation(text):
    """ This function accepts a text and fraction it into pieces"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    newline_required = True

    for char in text:
        if char in '.?:':
            result += char + "\n\n"
            newline_required = True
        else:
            if newline_required:
                if not char.isspace():
                    result += char
                    newline_required = False
            else:
                result += char

    print(result)
