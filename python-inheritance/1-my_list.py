#!/usr/bin/python3
"""defines a single subclass from parent list
"""

class MyList(list):
    """custom class that extends parent list with a single method
    """
    def print_sorted(self):
        """prints out the list in ascending order
        """
        copy = self.copy()
        copy.sort()
        print(copy)
        return copy
