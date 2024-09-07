#!/usr/bin/python3
"""this module carries a single geometric class
"""


class Square:
    """defines square objects with only one parameter
    """

    def __init__(self, size=0):
        """constructs a square with side of length `size`
        """
        self.size = size

    @property
    def size(self):
        """ returns the size of current square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """modifies the size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns the area of current square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints to stdout a square filed with #
        """
        if self.size != 0:
            for y in range(self.size):
                for x in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
