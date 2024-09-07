#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def add_integer(a, b=98):
    """adds two given intgers together
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    if abs(a) > 1000 or abs(b) > 1000:
        raise OverflowError("numbers exceed range of -1000 to 1000")
    return a + b
