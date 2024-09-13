#!/usr/bin/python3
"""defines a single class
"""


class Rectangle(BaseGeometry):
    """inherits and extends parent class
    """
    def __init__(self, width, height):
        try: 
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        else:
            self.__width = width
            self.__height = height
