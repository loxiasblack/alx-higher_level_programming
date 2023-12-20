#!/usr/bin/python3
"""!.base class module"""


class Base:
    """class for the object"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation with id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
