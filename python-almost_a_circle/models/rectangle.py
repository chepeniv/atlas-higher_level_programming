#!/usr/bin/python3
""" barebones module holding a single class
"""


from models.base import Base

class Rectangle(Base):
    """ foundational definition for Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer for Rectangle
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y
