#!/usr/bin/python3
"""python test script for Base class
    execute test :
        python3 -m unittest test.test_models.test_base
"""
import unittest
base = __import__('base').Base


class TestBaseClass(unittest.TestCase):
    """ class containing testing functions for Base class
        reference list of assert methods: 

        assertEqual(a, b)           a == b
        assertNotEqual(a, b)        a != b
        assertTrue(x)               bool(x) is True
        assertFalse(x)              bool(x) is False
        assertIs(a, b)              a is b
        assertIsNot(a, b)           a is not b
        assertIsNone(x)             a is None
        assertIsNotNone(x)          a is not None
        assertIn(a, b)              a in b
        assertNotIn(a, b)           a not in b
        assertIsInstance(a, b)      isinstance(a, b)
        assertNotIsInstance(a, b)   not isinstance(a, b)

        assertAlmostEqual(a, b)     round(a-b, 7) == 0
        assertNotAlmostEqual(a, b)  round(a-b, 7) != 0
        assertGreater(a, b)         a > b
        assertGreaterEqual(a, b)    a >= b
        assertLess(a, b)            a < b
        assertLessEqual(a, b)       a <= b
        assertRegex(s, r)           r.search(s)
        assertNotRegex(s, r)        not r.search(s)
        assertCountEqual(a, b)      a and b have the same number of each
                                    element (regardless of order)

        assertRaises(exc, fun, *args, **kwds)
        assertRaisesRegex(exc, r, fun, *args, **kwds)
        assertWarns(warn, fun, *args, **kwds)
        assertWarnsRegex(warn, r, fun, *args, **kwds)
        assertLogs(logger, level)
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
