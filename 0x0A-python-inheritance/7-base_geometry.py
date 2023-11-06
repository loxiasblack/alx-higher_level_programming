#!/usr/bin/python3
""" Improve Geometry"""


class BaseGeometry:
    """an empty Base geometry"""

    def area(self):
        """raise an exepction with the
        follow message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
