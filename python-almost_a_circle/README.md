# ALMOST A CIRCLE: 

## Overview

- importing
- exceptions
- classes
- private attributes
- getters/setters
- class methods
- static methods
- inheritance
- unittesting
- reading/writing files
- args and kwargs
- serialization/deserialization
- json

## Instructions

- create `Base` class
- create `Rectangle(Base)` class
- update `Rectangle`: add validation to all setter methods and instantiation (id excluded)
- update `Rectangle`: add public method `def area(self)` that returns area 
- update `Rectangle`: add public method `def display(self)` that prints to stdout the rectangle using the character # - no need to handle x and y 
- update `Rectangle`: override `str` method so that it returns [rectangle] instance
- update `Rectangle`: improve public method `def display(self)` to handle x and y
- update `Rectangle`: add public method `def update(self, *args)` to assign an argument to each attribute
- update `Rectangle`: update public method `def update(self, *args)` by changing the prototype to `update(self, *args, kwargs)` that assigns a key/value argument to attributes
- create `Square(Rectangle)` class
- update `Square`: add public getter and setter for `size`
- update `Square`: add public method `def update(self, *args, kwargs)` that assigns attributes
- update `Rectangle`: add public method `def to_dictionary(self)` that returns the dictionary representation of a rectangle
- update `Square`: add public method `def to_dictionary(self)` that returns the dictionary representation of a square
- update `Base`: add class method `def savetofile(cls, listobjs)` that writes the json string representation of listobjs to a file
- update `Base`: add static method `def fromjsonstring(jsonstring)` that returns the list of the json string representation jsonstring
- update `Base`: add class method `def create(cls, dictionary)` to return an instance with all attributes already set
- update `Base`: add class method `def loadfromfile(cls)` to return a list of instances

## Learning Objectives

- what is unit testing and how to implement it in a large project
- how to serialize and deserialize a class
- how to write and read a json file
- what is `*args` and how to use it
- what is `**kwargs` and how to use it
- how to handle named arguments in a function

## Testing

- use the `unittest` module
- test files should be inside the folder `tests`
- test files should be python .py files 
- test files should begin with `test_`
- test file organization should follow project file organization
- tests should be executable via `python3 -m doctest ./tests/*`
- run test files with :
	`python -m unittest discover tests`\
	or\
	`python -m unittest test/test_models/test_base.py`

## Documentation

documentation is not a single word, use complete sentences explaining what’s the purpose of the module, class or method
