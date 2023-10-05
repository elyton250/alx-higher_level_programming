#!/usr/bin/python3
"""this functions adds arguments"""
if __name__ == "__main__":
    from sys import argv
    t_sum = 0
    for i in range(1, len(argv)):
        int_val = int(argv[i])
        t_sum += int_val
    print(f"{t_sum}")
