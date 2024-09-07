#!/usr/bin/python3
"""this module carries a single geometric class
"""

class square:
    """defines square objects with only one parameter

    Attributes:
        size(int): denotes the length of any side of this square
    """
    def __init__(self, size):
        """creates a square object with only a single parameter

        Args:
            size(int): length of square's side
        """
        self.__size = size
