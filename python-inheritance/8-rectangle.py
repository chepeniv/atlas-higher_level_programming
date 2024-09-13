#!/usr/bin/python3
"""defines a single class
"""


class Rectangle(BaseGeometry):
    """inherits and extends parent class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
