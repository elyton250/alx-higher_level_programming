#!/usr/bin/python3
"""This module defines the class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """This class defines a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """it initialises a rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """this method calculates the area"""
        return self.height * self.width

    def display(self):
        """this functions prints the rectangle"""
        for _ in range(self.y):
            print("")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """thi prints the string"""
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        idd = self.id
        return f"[Rectangle] ({idd}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """this method updates the rectangle"""
        if args and len(args) > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns a dict representation of a rectangle"""
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        idd = self.id
        return {'id': idd, 'width': w, 'height': h, 'x': x, 'y': y}
