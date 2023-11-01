#!/usr/bin/python3
def add_integer(a, b=98):
    """
    >>> a = 2
    >>> add_integer(a, 2)
    4
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
