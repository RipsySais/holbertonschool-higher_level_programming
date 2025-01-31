#!/usr/bin/python3

""" Square class with size attribute"""


class Square:
    """ a square class"""
    def __init__(self, size=0):
        """ initializes the size attribute"""
        self.__size = size

    @property
    def size(self):
        """ returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """ prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
