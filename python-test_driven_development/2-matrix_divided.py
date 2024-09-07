#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def matrix_divided(matrix, div):
    """returns a duplicate matrix wherein each element is divided by div
    """
    # check that elements of matrix are integers or floats
    # otherwise raise TypeError("matrix must be a matrix (list of lists) of integer/floats")
    # each row of the matrix must be the same size
    # otherwise raise TypeError("Each row of the matrix must have the same size")
    # div must be an int or float
    # otherwiseh raise TypeError("div must be a number")
    # div != 0; otherwise raise ZeroDivisionError("division by zero")
    # return a duplicate matrix wherein each element is divided by div and rounded to two decimal places
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if abs(a) > 1000 or abs(b) > 1000:
        raise OverflowError("numbers exceed range of -1000 to 1000")
    return a + b
