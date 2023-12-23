#!/usr/bin/python3
"""!.base class module"""
import json


class Base:
    """class for the object"""
    __nb_objects = 0
    list_objs = []

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
        return json.dumps(list_dictionaries, default=lambda
                          list_dictionaries: list_dictionaries.__dict__)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that write Json string of my list_objt"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_obj = []
        jsonstr = cls.to_json_string([inst.to_dictionary()
                                      for inst in list_objs])
        with open(filename, "w") as f:
            f.write(jsonstr)
