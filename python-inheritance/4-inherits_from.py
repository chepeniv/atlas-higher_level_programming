#!/usr/bin/python3
"""defines a single function
"""


def inherits_from(obj, kind):
    """test whether or not the given obj is an instance of given class kind
    """
    return issubclass(type(obj), kind) and not isinstance(obj, kind)
