#!/usr/bin/python3
"""2.First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """this a class for Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """retrive the width"""

        return self.__width

    @width.setter
    def set_width(self, value):
        """set the value to the width"""

        self.__width = value

    @property
    def height(self):
        """Retreive the height"""

        return self.__height

    @height.setter
    def set_height(self, value):
        """set a value to the height"""

        self.__height = value

    @property
    def x(self):
        """retreive x"""

        return self.__x

    @x.setter
    def set_x(self, value):
        """set the value to x"""

        self.__x = value

    @property
    def y(self):
        """Retreive y"""

        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""

        self.__y = value
