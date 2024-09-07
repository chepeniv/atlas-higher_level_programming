#!/usr/bin/python3
"""this module carries a single geometric class
"""


class Square:
    """defines square objects with only one parameter
    """

    def __init__(self, size=0, position=(0, 0)):
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
        """sets the horizontal and vertical offset of the square
        """
        if len(position) == 2:
            h = position[0]
            v = position[1]
            if (type(h), type(v)) == (int, int):
                if (h >= 0) and (v >= 0):
                    self.__position = position
                    return
        self.__pos_error()

    def area(self):
        """ returns the area of current square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints to stdout a square filed with # and
        with whitespace by self.position
        """
        if self.size != 0:
            for vertical_offset in range(self.position[1]):
                print()
            for height in range(self.size):
                for horizontal_offset in range(self.position[0]):
                    print(" ", end='')
                for length in range(self.size):
                    print("#", end='')
                print()
        else:
            print()

    def __pos_error(self):
        """ raises custom TypeError
        """
        raise TypeError("position must be a tuple of 2 positive integers")
