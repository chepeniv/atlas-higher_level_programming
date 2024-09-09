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

    def __str__(self):
        """constructs and returns an ascii string rendering based
        of the current rectangle's width and height
        """
        render = ""
        for row in range(self.height - 1):
            render += "#" * self.width + "\n"
        render += "#" * self.width
        return render


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
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """modifies the height of current Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculate and return the area of the current rectangle
        """
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2 * self.width) + (2 * self.height)