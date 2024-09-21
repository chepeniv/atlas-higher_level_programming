#!/usr/bin/python3

from models.rectangle import Rectangle
from models.square import Square
from models.base import Base

r1 = Rectangle(10, 7, 2, 8)
r2 = Rectangle(2, 4)
list_rectangles_input = [r1, r2]

Rectangle.save_to_file(list_rectangles_input)

list_rectangles_output = Rectangle.load_from_file()

print("print call - 1")
for rect in list_rectangles_input:
    print("[{}] {}".format(id(rect), rect))

print("print call - 2")
for rect in list_rectangles_output:
    print("[{}] {}".format(id(rect), rect))

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file(list_squares_input)

list_squares_output = Square.load_from_file()

print("print call - 3")
for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("print call - 4")
for square in list_squares_output:
    print("[{}] {}".format(id(square), square))
