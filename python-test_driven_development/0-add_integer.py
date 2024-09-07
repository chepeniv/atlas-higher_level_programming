#!/usr/bin/python3
"""practicing TDD given a single function 
"""


def add_integer(a, b=98):
    """adds two given intgers together

    testing considerations - checking type, testing range
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    return a + b
