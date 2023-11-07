#!/usr/bin/python3
""""this a file that read lines from file text"""


def read_file(filename=""):
    """read file entered"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
