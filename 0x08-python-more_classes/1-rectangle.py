#!/usr/bin/python3
"""1. Real definition of a rectangle

This module creates a class Rectangle that defines a rectangle by:

Private instance attribute: width:
 -property def width(self): to retrieve it
 -property setter def width(self, value): to set it:
    *width must be an integer, otherwise raise a TypeError exception
    with the message width must be an integer
    *if width is less than 0, raise a ValueError exception with the
    message width must be >= 0
Private instance attribute: height:
 -property def height(self): to retrieve it
 -property setter def height(self, value): to set it:
    *height must be an integer, otherwise raise a TypeError exception with
    the message height must be an integer
    *if height is less than 0, raise a ValueError exception with the message
    height must be >= 0
Instantiation with optional width and height:
def __init__(self, width=0, height=0):
"""


class Rectangle:
    """class for the Rectangle object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve the width"""
        return self.__width

    @property
    def height(self):
        """property to retrieve the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """property to set the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """property to set the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
