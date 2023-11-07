#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """append to a file text"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
