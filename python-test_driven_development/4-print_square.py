#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def print_square(size):
    """output a square made out of # based on size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("{}".format('#' * size))
