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
    for item in range(len(text) - 1):
        line = text[item]
        print(line.strip())
    line = text[-1]
    print(line.strip(), end='')
