#!/usr/bin/python3
"""defines a single function
"""


def is_same_class(obj, a_class):
    """test whether or not the given obj is exactly and instance of a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
