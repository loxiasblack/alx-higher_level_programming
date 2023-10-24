#!/usr/bin/python3
"""1. Square with size

This module creates a class Square that defines a square by:
 (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
"""


class Square:
    """Class for the Square object"""
    def __init__(self, size=None):
        self.__size = size
