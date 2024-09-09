#!/usr/bin/python3
"""a practice implementation of unittest
run this using: python3 -m unittest test.6-max_integer_test
"""
import unittest
max_int = __import__('6-max_integer').max_integer


class TestMaxIntFunc(unittest.TestCase):
    """class containing all testing functions for max_integer
    """
    def test_max_at_end(self):
        self.assertEqual(max_int([0, 1, 2]), 2)
    def test_max_at_start(self):
        self.assertEqual(max_int([2, 1, 0]), 2)
    def test_max_at_middle(self):
        self.assertEqual(max_int([2, 4, 1]), 4)
    def test_one_negative(self):
        self.assertEqual(max_int([1, 0, -1]), 1)
    def test_only_negative(self):
        self.assertEqual(max_int([-1, -6, -12]), -1)
    def test_single_element(self):
        self.assertEqual(max_int([3]), 3)
    def test_empty(self):
        self.assertEqual(max_int([]), None)

    if __name__== '__main__':
        unittest.main()
