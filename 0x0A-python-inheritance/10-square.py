#!/usr/bin/python3
"""Module that defines a class Square
    that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with szie:
        size must be private. No getter or setter
        size must be a positive integer, validated
        by integer_validator"""
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
