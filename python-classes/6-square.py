#!/usr/bin/python3
"""this module carries a single geometric class
"""


class Square:
    """defines square objects with only one parameter
    """

    def __init__(self, size=0, position=(0,0)):
        """constructs a square with side of length `size`
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """ returns the size of current square
        """
        return self.__position

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

    @position.setter
    def position(self, position):
        """modifies the size of the square
        """
        h = position[0]
        v = position[1]
        if type(position) is not tuple and type(h) is not int and type(v) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """ returns the area of current square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints to stdout a square filed with # and
        with whitespace by self.position
        """
        for vertical_offset in range(self.position[1]):
            print()
        if self.size != 0:
            for height in range(self.size):
                for horizontal_offset in range(self.position[0]):
                    print(" ", end='')
                for length in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
