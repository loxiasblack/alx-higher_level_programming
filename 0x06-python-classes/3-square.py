#!/usr/bin/python3
"""3. Area of a square

This module creates a class Square that defines a square by:

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
- size must be an integer, otherwise raise a TypeError exception with the
message size must be an integer
- if size is less than 0, raise a ValueError exception with the message size
must be >= 0
Public instance method: def area(self): that returns the current square area
"""


class Square:
    """Class for the Square object"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return self.__size**2