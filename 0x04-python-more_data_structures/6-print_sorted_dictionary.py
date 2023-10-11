#!/usr/bin/pyhton3
def print_sorted_dictionary(a_dictionary):
    sortedDict = sorted(a_dictionary.items())
    for keys, value in sortedDict:
        print(f"{keys}: {value}")
