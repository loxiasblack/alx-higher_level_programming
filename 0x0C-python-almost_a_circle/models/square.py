#!/usr/bin/python3
"""10. And now, the Square!"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """New class of square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation of square object"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y}"
                f" - {self.height}")

    @property
    def size(self):

        return self.size

    @size.setter
    def size(self, value):

        self.__width = value
        self.__height = value

        """retreive the size"""
        return self.height

    @size.setter
    def size(self, value):
        """set a value to the size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """update the attribute"""
        counter = 0
        if not args:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
        for arg in args:
            if counter == 0:
                self.id = args[0]
            if counter == 1:
                self.size = arg
            if counter == 2:
                self.x = arg
            if counter == 3:
                self.y = arg
            counter += 1

    def to_dictionary(self):
        """ method that return a dict of square attribute """
        return {
                "id": self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
                }
