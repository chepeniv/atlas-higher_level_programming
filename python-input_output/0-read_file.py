#!/usr/bin/python3
"""defines a single function
"""


def lookup(obj):
    """returns a list of available attributes and methods of the given object
    """
    return dir(obj)
