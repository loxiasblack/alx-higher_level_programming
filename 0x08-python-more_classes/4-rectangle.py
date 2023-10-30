#!/usr/bin/python3
"""2. Area and Perimeter"""


class Rectangle:
    """class for the Rectangle object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """property to retrieve the width"""
        return self.__width

    @property
    def height(self):
        """property to retrieve the height"""
        return self.__height

    @width.setter
    def width(self, value):
        """property to set the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """property to set the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the current rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """string format of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ''
        return ("#" * self.__width + "\n") * (self.__height - 1)\
            + ("#" * self.__width)

    def __repr__(self):
        """String representation of the rectangle for eval"""
        return f"Rectangle({self.width}, {self.__height})"
