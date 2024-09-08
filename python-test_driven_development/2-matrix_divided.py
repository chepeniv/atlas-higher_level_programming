#!/usr/bin/python3
"""module with a single function to use doctest on
"""


def matrix_divided(matrix, div):
    """returns a duplicate matrix wherein each element is divided by div
    """
    width = len(matrix[0])
    for row in matrix:
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if width != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    duplicate = []
    for row in matrix:
        row = map(lambda n: round(n / div, 2), row)
        duplicate.append(list(row))

    return duplicate
