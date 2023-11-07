#!/usr/bin/python3
"""write text in file"""


def write_file(filename="", text=""):
    """function that allow to write a text and return the """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
