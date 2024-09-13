#!/usr/bin/python3
"""defines a single function for file i/o
"""


def append_write(filename="", text=""):
    """appends plaintext to a given utf-8 textfile
    returns total characters added
    """
    with open(filename, mode="a") as file:
        file.write(text)

    return len(text)
