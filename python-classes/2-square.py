#!/usr/bin/python3

""" This module defines a class Square."""


class Square:
    """ A class to represent a square."""
    def __init__(self, size=0):
        """ Initialize the class with a size."""
        self.size = size

    @property
    def size(self):
        """ Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return the area of the square."""
        return self.__size
