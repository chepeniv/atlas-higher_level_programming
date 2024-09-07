#!/usr/bin/python3
"""this module carries a single geometric class
"""


class Square:
    """defines square objects with only one parameter
    """
    def __init__(self, size):
        """constructs a square with side of length `size`
        """
        self.__size = size
