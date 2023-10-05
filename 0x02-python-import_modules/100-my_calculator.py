#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv
    if len(argv) != 4:
        print("{}".format("Usage: ./100-my_calculator.py <a> <operator> <b>"))
        exit(1)
    elif argv[2] == "+" or argv[2] == "-" or argv[2] == "*" or argv[2] == "/":
        a = int(argv[1])
        b = int(argv[3])
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        if argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        if argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        if argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
