#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def say_my_name(first, last=""):
    """impersonate the user 
    """
    #if neither first or last are strings 
    #       raise TypeError("{part} must be a string")
    if type(first) is not str:
        raise TypeError("first_name must be a string")
    if type(last) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first, last))
