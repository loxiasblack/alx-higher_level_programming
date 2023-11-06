#!/usr/bin/python3
"""Module that defines a class
MyInt that inherits from in"""


class MyInt(int):
    """class MyInt that inherits from in"""

    def __ne__(self, value):
        """inverse != with =="""
        return self.real == value

    def __eq__(self, value):
        """reverse == with !="""
        return self.real != value
