#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def add_integer(a, b=98):
    """adds two given intgers together
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if abs(a) > 1000 or abs(b) > 1000:
        raise OverflowError("numbers exceed range of -1000 to 1000")
    return a + b
