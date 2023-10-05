#!/usr/bin/python3
from sys import argv
a = len(argv)
b = a - 1
if a == 1:
    print(f"0 arguments.")
elif a == 2:
    print(f"{b} argument:")
    print(f"{b}: {argv[b]}")
elif a > 2:
    print(f"{b} arguments:")
    for i in range(1, a):
        print(f"{i}: {argv[i]}")
