#!/usr/bin/python3
"""a practice implementation of unittest
run this using: python3 -m unittest test.6-max_integer_test
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxIntFunc(unittest.TestCase):
    """class containing all testing functions for max_integer
    """
    def test_expected_use(self):
        self.assertEqual(max_int([0, 1, 2]), 2)
        self.assertEqual(max_int([2, 1, 0]), 2)
        self.assertEqual(max_int([-1, 0, 1]), 1)
        self.assertEqual(max_int([1, 0, -1]), 1)

    if __name__== '__main__':
        unittest.main()
