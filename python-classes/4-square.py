#!/usr/bin/python3

""" Square class with size attribute"""


class Square:
    """ a square class"""
    def __init__(self, size=0):
        """ initializes the size attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
