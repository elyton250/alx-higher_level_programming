#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delkeysList = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            delkeysList.append(key)
    for key in delkeysList:
        del a_dictionary[key]
    return a_dictionary
