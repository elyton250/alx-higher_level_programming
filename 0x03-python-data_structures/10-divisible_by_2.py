#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resList = []
    for i in my_list:
        if i % 2 == 0:
            resList.append(True)
        else:
            resList.append(False)
    return resList
