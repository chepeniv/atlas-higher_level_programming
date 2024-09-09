#!/usr/bin/python3
"""module with a single function to use unittest on
"""


def max_integer(numlist=[]):
    """find and return the largest integer in the given list
    """
    if len(numlist) == 0:
        return None
    
    result = numlist[0]
    index = 1
    while index < len(numlist):
        if numlist[index] > result:
            result = numlist[index]
        index += 1

    return result

