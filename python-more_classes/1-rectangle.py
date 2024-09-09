#!/usr/bin/python3
"""this module contains a single geometric class
"""


class Rectangle:
    """defines rectangle objects
    """
    def __init__(self, width=0, height=0):
        """constructs rectangle object with given width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of current Rectangle
        """
        return self.__width

    @property
    def height(self):
        """returns the height of current Rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """modifies the width of current Rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must >= 0")
        else:
            self.__width = value


    @height.setter
    def height(self, value):
        """modifies the height of current Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must >= 0")
        else:
            self.__height = value
