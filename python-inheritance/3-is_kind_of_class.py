#!/usr/bin/python3
"""defines a single function
"""


def is_kind_of_class(obj, kind):
    """test whether or not the given obj is an instance of given class kind
    """
    return issubclass(type(obj), kind)
