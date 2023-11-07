#!/usr/bin/python3
"""10. Student to JSON with filter"""


class Student:
    """class for the Student object"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        Otherwise, all attributes must be retrieved"""
        if (isinstance(attrs, list) and
                all(isinstance(e, str) for e in attrs)):
            return {e: getattr(self, e) for e in attrs if hasattr(self, e)}
        return self.__dict__

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance"""
        for key, val in json.items():
            if hasattr(self, key):
                setattr(self, key, val)
