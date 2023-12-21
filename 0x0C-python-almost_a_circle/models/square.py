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
