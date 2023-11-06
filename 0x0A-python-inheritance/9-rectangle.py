#!/usr/bin/python3
"""Module that defines a class Rectangle
    that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Derived class from Base Geometry"""

    def __init__(self, width, height):
        """width and height must be private.and
        they must be positive and integers"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def __str__(self):
        """string format"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
