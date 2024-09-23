#!/usr/bin/python3
""" python test script for Base class
    execute test :
        python3 -m unittest test.test_models.test_base
    or
        python3 -m unittest test/test_models/test_base.py

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


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """ class containing testing functions for Base class
    """

    def test_base_id(self):
        base = Base()
        self.assertIsNotNone(base.id)

    def test_base_id_increment(self):
        base_A = Base()
        base_B = Base()
        self.assertEqual(base_A.id + 1, base_B.id)

    def test_base_id_assignment(self):
        base = Base(89)
        self.assertEqual(base.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    # def test_from_json_string_exist(self):
    # def test_from_json_string_list_exist(self):


class TestRectangleClass(unittest.TestCase):
    """ class containing testing functions for Base class
    """

    def test_rect_2_params(self):
        rectA = Rectangle(1, 2)
        self.assertEqual(rectA.width, 1)
        self.assertEqual(rectA.height, 2)

    def test_rect_3_params(self):
        rectB = Rectangle(1, 2, 3)
        self.assertEqual(rectB.x, 3)

    def test_rect_4_params(self):
        rectC = Rectangle(1, 2, 3, 4)
        self.assertEqual(rectC.y, 4)

    def test_rect_5_params(self):
        rectD = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rectC.id, 5)

    def test_rect_wrong_param_1(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("W", 2)

    def test_rect_wrong_param_2(self):
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(1, "H")

    def test_rect_wrong_param_3(self):
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(1, 2, "X")

    def test_rect_wrong_param_4(self):
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(1, 2, 3, "Y")

    def test_rect_neg_param_1(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-1, 2)

    def test_rect_neg_param_2(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -2)

    def test_rect_neg_param_3(self):
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 2, -3)

    def test_rect_neg_param_4(self):
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 2, 3, -4)

    def test_rect_zero_param_1(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)

    def test_rect_zero_param_2(self):
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)

    def test_rect_area(self):
        rect = Rectangle(3, 3)
        self.assertIsInstance(rect.area(), int)

if __name__== '__main__':
    unittest.main()
