#!/usr/bin/python3

"""7. Change representation"""


class Rectangle():
    """class for the Rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = width
        else:
            raise TypeError("width must be an integer")
        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = height
        else:
            raise TypeError("height must be an integer")
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property to retrieve the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """property to set the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property to retrieve the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """property to set the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the current rectangle area"""

        return self.__height * self.__width

    def perimeter(self):
        """returns the current rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """class method to return square"""
        return cls(size, size)

    def __str__(self) -> str:
        """String representation of an instanc of the Rectangle object
        Uses # to print it
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        return (str(self.print_symbol) * self.__width + "\n") * \
            (self.__height - 1) + (str(self.print_symbol) * self.__width)

    def __repr__(self):
        """String representation of the rectangle for eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete the Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
