#!/usr/bin/python3
"""this module definees a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """this class inherits the recatngle and defines the square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this returns represtantiomn of square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """this is getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """this is a setter for size and size is already checked"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """this method assigns attributes"""
        attributes = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dict represantation of the square"""
        idd = self.id
        size = self.size
        x = self.x
        y = self.y
        return {'id': idd, 'size': size, 'x': x, 'y': y}
