#!/usr/bin/python3
"""5. Printing a square

This module creates a class Square that defines a square by:

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
-size must be an integer, otherwise raise a TypeError exception with the
message size must be an integer
-if size is less than 0, raise a ValueError exception with the message size
must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self):
-that prints in stdout the square with the character #:
-if size is equal to 0, print an empty line
"""


class Square:
    """Class for the Square object"""
    def __init__(self, size=0):
        """Instantiation of a square instance"""
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """property to retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value=None):
        """property to set the size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
