#!/usr/bin/python3
""" python test script for Rectangle class
    execute test :
        python3 -m unittest test.test_rectangle
    or
        python3 -m unittest test/test_rectangle.py

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

    assertRaises(exc, fun, *args, **kwds)
    assertRaisesRegex(exc, r, fun, *args, **kwds)
    assertWarns(warn, fun, *args, **kwds)
    assertWarnsRegex(warn, r, fun, *args, **kwds)
    assertLogs(logger, level)
"""


import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ class containing testing functions for Base class
    """

    def test_rectangle_init_2_params(self):
        rectA = Rectangle(1, 2)
        self.assertEqual(rectA.width, 1)
        self.assertEqual(rectA.height, 2)

    def test_rectangle_init_3_params(self):
        rectB = Rectangle(1, 2, 3)
        self.assertNotEqual(rectB.x, 0)
        self.assertEqual(rectB.x, 3)

    def test_rectangle_init_4_params(self):
        rectC = Rectangle(1, 2, 3, 4)
        self.assertNotEqual(rectC.y, 0)
        self.assertEqual(rectC.y, 4)

if __name__== '__main__':
    unittest.main()
