#!/usr/bin/python3
"""!.base class module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that return representation of my list_dictionary"""
        if list_dictionaries is None:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)
