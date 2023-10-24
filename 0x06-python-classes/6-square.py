#!/usr/bin/python3
"""6. Coordinates of a square

This module creates a class Square that defines a square by:

Private instance attribute: size:
- property def size(self): to retrieve it
- property setter def size(self, value): to set it:
    * size must be an integer, otherwise raise a TypeError exception with the
    message size must be an integer
    * if size is less than 0, raise a Value Error exception with the message
    size must be >= 0
Private instance attribute: position:
- property def position(self): to retrieve it
- property setter def position(self, value): to set it:
    * position must be a tuple of 2 positive integers, otherwise raise a
    TypeError exception with the message position must be a tuple of 2 positive
    integers
Instantiation with optional size and optional position:
def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square
with the character #:
- if size is equal to 0, print an empty line
- position should be use by using space - Don’t fill lines by spaces when
position[1] > 0
"""


class Square:
    """Class for the Square object"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation of a square instance"""
        err = 0
        err_mes = "position must be a tuple of 2 positive integers"
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (not isinstance(position, tuple) or len(position) != 2 or
                any(not isinstance(e, int) or e < 0 for e in position)):
            raise TypeError(err_mes)
        else:
            self.__position = position

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(self.__position[0] * " ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    @property
    def size(self):
        """property to retrieve the size"""
        return self.__size

    @property
    def position(self):
        """property to retrieve the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """property to set the size"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """property to set the position"""
        err_mes = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple) or len(value) != 2 or
                any(not isinstance(e, int) or e < 0 for e in value)):
            raise TypeError(err_mes)
        else:
            self.__position = value
