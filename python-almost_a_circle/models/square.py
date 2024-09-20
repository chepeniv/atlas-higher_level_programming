#!/usr/bin/python3
""" barebones module holding a single class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ foundational definition for Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializer for Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        obj_str = "[Square] ({}) {}/{} - {}"
        return obj_str.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
