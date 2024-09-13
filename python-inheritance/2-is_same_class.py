#!/usr/bin/python3
"""defines a single function
"""


def is_same_class(obj, kind):
    """test whether or not the given obj is exactly and instance of kind
    this might have worked, but i didn't test it: return isinstance(obj, kind)
    """
    if type(obj) is kind:
        return True
    else:
        return False
