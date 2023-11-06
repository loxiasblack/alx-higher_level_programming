#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """the class list"""
    def print_sorted(self):
        """sorted the list"""
        print(sorted(self))
