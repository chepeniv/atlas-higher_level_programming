#!/usr/bin/python3
""" barebones module holding a single class
"""


from rectangle import Rectangle


class Square(Rectangle):
    """ foundational definition for Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ initializer for Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        obj_str = "[Square] ({}) {}/{} - {}"
        return obj_str.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ modifies the values of the current object based either on argument
        position or keywords
        """
        keys = ['id', '_Rectangle__width', '_Rectangle__x', '_Rectangle__y']
        argkeys = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for item in range(len(args)):
                self.__dict__.update({keys[item]: args[item]})
        else:
            for item in range(4):
                value = kwargs.get(argkeys[item])
                if value is not None:
                    self.__dict__.update({keys[item]: value})

    def to_dictionary(self):
        """ construct and return a dictionary of the current
        object's properties
        """
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
