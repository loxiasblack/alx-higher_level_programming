#!/usr/bin/python3
"""function that adds a new attribute
to an object if  possible"""


def add_attribute(obj, att, value):
    """function that adds a new attribute
    to an object if its possible:

    Raise a TypeError exception, with the message
    can't add new attribute if the object cant have
    new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[att] = value
