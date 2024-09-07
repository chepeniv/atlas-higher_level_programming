#!/usr/bin/python3
"""this module carries a single geometric class
"""


class Square:
    """defines square objects with only one parameter
    """
    def __init__(self, size=0):
        """constructs a square with side of length `size`
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
