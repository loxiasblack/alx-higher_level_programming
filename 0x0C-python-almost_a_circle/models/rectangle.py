#!/usr/bin/python3
"""2.First Rectangle"""
from models.base import Base


class Rectangle(Base):
    """this a class for Rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """retrive the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """set the value to the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retreive the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """set a value to the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retreive x"""

        return self.__x

    @x.setter
    def x(self, value):
        """set the value to x"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retreive y"""

        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that return area of rectangle"""
        return self.__height * self.__width

    def display(self):
        """method that display rectangle with #"""
        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    def update(self, *args):
        """function that update the attribute"""
        counter = 0
        for arg in args:
            if counter == 0:
                self.id = args[0]
            if counter == 1:
                self.__width = arg
            if counter == 2:
                self.__height = arg
            if counter == 3:
                self.__x = arg
            if counter == 4:
                self.__y = arg
            counter += 1
