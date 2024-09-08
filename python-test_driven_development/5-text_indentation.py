#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def text_indentation(text):
    """outputs the given text, but with 2 empty lines after
    each ., ?, and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")
    text = text.splitlines(True)
    for line in text:
        print(line.strip())
