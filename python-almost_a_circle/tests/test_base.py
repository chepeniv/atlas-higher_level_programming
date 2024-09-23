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


class TestBaseClass(unittest.TestCase):
    """ class containing testing functions for Base class
    """

    def test_base_id(self):
        base = Base()
        self.assertEqual(base.id, 1)

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

if __name__== '__main__':
    unittest.main()