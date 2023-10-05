#!/usr/bin/python3
"""this function is a caculator"""
if __name__ == "__main__":
    import calculator_1
    from sys import argv
    arg_len = len(argv)
    if arg_len < 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    if operator == '+':
        print(f"{a} {argv[2]} {b} = {calculator_1.add(a, b)}")
    elif operator == '-':
        print(f"{a} {argv[2]} {b} = {calculator_1.sub(a, b)}")
    elif operator == '*':
        print(f"{a} {argv[2]} {b} = {calculator_1.mul(a, b)}")
    elif operator == '/':
        print(f"{a} {argv[2]} {b} = {calculator_1.div(a, b)}")
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
