#!/usr/bin/python3
"""defines a single function for file i/o
"""


def read_file(filename=""):
    """reads from given utf-8 textfile 
    """
    with open(filename) as file:
        text = file.read()
        print(text, end='')
