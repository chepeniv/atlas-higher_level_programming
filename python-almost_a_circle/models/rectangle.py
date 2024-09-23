#!/usr/bin/python3
""" barebones module holding a single class
"""


from base import Base


class Rectangle(Base):
    """ foundational definition for Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializer for Rectangle
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        obj_str = "[Rectangle] ({}) {}/{} - {}/{}"
        return obj_str.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ calculates and returns the area of the current Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """outputs to stdout a #-filled representation of the Rectangle object
        """
        for row in range(self.y):
            print()
        for row in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args, **kwargs):
        """ modifies the values of the current object based either on argument
        position or keywords
        """
        keys = ['id', '_Rectangle__width', '_Rectangle__height',
                '_Rectangle__x', '_Rectangle__y']
        argkeys = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for item in range(len(args)):
                self.__dict__.update({keys[item]: args[item]})
        else:
            for item in range(5):
                value = kwargs.get(argkeys[item])
                if value is not None:
                    self.__dict__.update({keys[item]: value})

    def to_dictionary(self):
        """ construct and return a dictionary of the current
        object's properties
        """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
