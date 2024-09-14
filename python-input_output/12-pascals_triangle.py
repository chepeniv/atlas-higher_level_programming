#!/usr/bin/python3
"""defines a single mathematical function
"""


def pascal_triangle(n):
    """prints out a pascal's triangle of height n
    """
    triangle = []

    if n > 0: 
        triangle.append([1])
        for line in range(n - 1):
            prev = triangle[-1]
            new = [1]
            for item in range(len(prev) - 1):
                value = prev[item] + prev[item + 1]
                new.append(value)
            new.append(1)
            triangle.append(new)
