#!/usr/bin/python3
"""defines a single function for file i/o
"""


def write_file(filename="", text=""):
    """writes plaintext to a given utf-8 textfile
    """
    with open(filename, mode="w") as file:
        file.write(text)
        return len(text)
