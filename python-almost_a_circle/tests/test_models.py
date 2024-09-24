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


import sys, io, os, contextlib, unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

def setUpModule():
    pass

def tearDownModule():
    pass

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

    def tearDown(self):
        if os.path.isfile("Rectangle.json"):
            os.remove("Rectangle.json")

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
        self.assertEqual(rectD.id, 5)

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
        self.assertEqual(rect.area(), 9)

    def test_rect__str__(self):
        rect = Rectangle(3, 3)
        self.assertEqual(str(rect), "[Rectangle] ({}) 0/0 - 3/3".format(rect.id))

    def test_rect_display(self):
        rect = Rectangle(3, 3)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue().strip()
        self.assertEqual(output, "###\n###\n###")

    def test_rect_display(self):
        rect = Rectangle(3, 3)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue().strip()
        self.assertEqual(output, "###\n###\n###")

    def test_rect_display_with_x(self):
        rect = Rectangle(3, 3, 4)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue()
        self.assertEqual(output, "    ###\n    ###\n    ###\n")

    def test_rect_display_with_x_y(self):
        rect = Rectangle(3, 3, 4, 4)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            rect.display()
        output = output.getvalue()
        self.assertEqual(output, "\n\n\n\n    ###\n    ###\n    ###\n")

    def test_rect_to_dict(self):
        rect = Rectangle(4, 4)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': rect.id, 'width': 4, 'height': 4, 'x': 0, 'y': 0})

    def test_rect_update(self):
        rect = Rectangle(4, 4)
        self.assertIsNone(rect.update())

    def test_rect_update_pos_1(self):
        rect = Rectangle(4, 4)
        rect.update(89)
        self.assertEqual(rect.id, 89)

    def test_rect_update_pos_2(self):
        rect = Rectangle(4, 4)
        rect.update(89, 1)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': 89, 'width': 1, 'height': 4, 'x': 0, 'y': 0})

    def test_rect_update_pos_3(self):
        rect = Rectangle(4, 4)
        rect.update(89, 1, 2)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': 89, 'width': 1, 'height': 2, 'x': 0, 'y': 0})

    def test_rect_update_pos_4(self):
        rect = Rectangle(4, 4)
        rect.update(89, 1, 2, 3)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 0})

    def test_rect_update_pos_5(self):
        rect = Rectangle(4, 4)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(
                rect.to_dictionary(),
                {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})

    """i omited assert-testing on .update() with kwargs
    since the checker passed those
    """

    def test_rect_create_id(self):
        self.assertIsInstance(Rectangle.create(**{ 'id': 89}), Rectangle)

    def test_rect_create_id_width(self):
        self.assertIsInstance(Rectangle.create(
            **{ 'id': 89,
                'width': 1
               }), Rectangle)

    def test_rect_create_id_width_height(self):
        self.assertIsInstance(Rectangle.create(
            **{ 'id': 89,
                'width': 1,
                'height': 2
               }), Rectangle)

    def test_rect_create_id_width_height_x(self):
        self.assertIsInstance(Rectangle.create(
            **{ 'id': 89,
                'width': 1,
                'height': 2,
                'x': 3
               }), Rectangle)

    def test_rect_create_id_width_height_x_y(self):
        self.assertIsInstance(Rectangle.create(
            **{ 'id': 89,
                'width': 1,
                'height': 2,
                'x': 3,
                'y': 4
               }), Rectangle)

    def test_rect_save_to_file_none(self):
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", 'r') as jfile:
            jdata = jfile.read()
        self.assertEqual(jdata, "[]")
        self.assertIsInstance(jfile, io.TextIOWrapper)
        """
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertIsNone(Rectangle.save_to_file(None))
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_rect_save_to_file_empty(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertIsNone(Rectangle.save_to_file([]))
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_rect_save_to_file_one_object(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertIsNone(Rectangle.save_to_file([Rectangle(1, 2)]))
        self.assertTrue(os.path.isfile("Rectangle.json"))

    def test_rect_load_from_file_doesnt_exist(self):
        self.assertFalse(os.path.isfile("Rectangle.json"))
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_rect_load_from_file_exist(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.isfile("Rectangle.json"))
        self.assertNotEqual(Rectangle.load_from_file(), [])

class TestSquareClass(unittest.TestCase):
    """ class containing testing functions for Base class
    """

    def tearDown(self):
        if os.path.isfile("Square.json"):
            os.remove("Square.json")

    def test_square_params(self):
        square = Square(1)
        self.assertEqual(square.size, 1)

        square = Square(1, 2)
        self.assertEqual(square.x, 2)

        square = Square(1, 2, 3)
        self.assertEqual(square.y, 3)

        square = Square(1, 2, 3, 4)
        self.assertEqual(square.id, 4)

    def test_square_wrong_params(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square("s")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            Square(1, "x")

        with self.assertRaises(TypeError, msg="y must be an integer"):
            Square(1, 2, "y")

    def test_square_zero_params(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(0)

    def test_square_neg_params(self):
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-1)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Square(1, -2)

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Square(1, 2, -3)

    def test_square__str__(self):
        sq = Square(4)
        self.assertEqual(str(sq), "[Square] ({}) 0/0 - 4".format(sq.id))

    def test_square_to_dict(self):
        sq = Square(4)
        self.assertEqual(
                sq.to_dictionary(),
                {'id': sq.id, 'size': 4, 'x': 0, 'y': 0})

    def test_square_update_pos(self):
        sq = Square(4)
        self.assertIsNone(sq.update())

        sq.update(89)
        self.assertEqual(sq.id, 89)

        sq.update(89, 1)
        self.assertEqual(sq.size, 1)

        sq.update(89, 1, 2)
        self.assertEqual(sq.x, 2)

        sq.update(89, 1, 2, 3)
        self.assertEqual(sq.y, 3)

        """ the checker automatically passes the keyword argument test-cases
        """

    def test_square_create(self):
        self.assertIsInstance(Square.create(**{ 'id': 89}), Square)

        self.assertIsInstance(Square.create(
            **{ 'id': 89,
                'size': 1
               }), Square)

        self.assertIsInstance(Square.create(
            **{ 'id': 89,
                'size': 1,
                'x': 2
               }), Square)

        self.assertIsInstance(Square.create(
            **{ 'id': 89,
                'size': 1,
                'x': 2,
                'y': 3
               }), Square)

    def test_square_save_to_file_none(self):
        self.assertFalse(os.path.isfile("Square.json"))
        self.assertIsNone(Square.save_to_file(None))
        self.assertTrue(os.path.isfile("Square.json"))

    def test_square_save_to_file_empty(self):
        self.assertFalse(os.path.isfile("Square.json"))
        self.assertIsNone(Square.save_to_file([]))
        self.assertTrue(os.path.isfile("Square.json"))

    def test_square_save_to_file_one_object(self):
        self.assertFalse(os.path.isfile("Square.json"))
        self.assertIsNone(Square.save_to_file([Square(1, 2)]))
        self.assertTrue(os.path.isfile("Square.json"))

    def test_square_load_from_file_doesnt_exist(self):
        self.assertFalse(os.path.isfile("Square.json"))
        self.assertEqual(Square.load_from_file(), [])

    def test_square_load_from_file_exist(self):
        Square.save_to_file([Square(1, 2)])
        self.assertTrue(os.path.isfile("Square.json"))
        self.assertNotEqual(Square.load_from_file(), [])

if __name__== '__main__':
    unittest.main()
