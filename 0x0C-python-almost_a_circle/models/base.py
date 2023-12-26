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
        return json.dumps(list_dictionaries, default=lambda
                          list_dictionaries: list_dictionaries.__dict__)

    @staticmethod
    def from_json_string(json_string):
        """ return json string to dictionaries"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that write Json string of my list_objt"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        jsonstr = cls.to_json_string([inst.to_dictionary()
                                      for inst in list_objs])
        with open(filename, "w") as f:
            f.write(jsonstr)

    @classmethod
    def create(cls, **dictionary):
        """creat a dummy instance"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            Base.just_dummy()
        if cls.__name__ == "Square":
            dummy = cls(1)
            Base.just_dummy()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def just_dummy(cls):
        """ignore the count"""
        Base.__nb_objects -= 1

    @classmethod
    def load_from_file(cls):
        if cls.__name__ == "Rectangle":
            with open("Rectangle.json", "r") as f:
                list_data = json.load(f)
            return list_data
        if cls.__name__ == "Square":
            with open("Square.json", "r") as f:
                data = json.load(f)
            return data
