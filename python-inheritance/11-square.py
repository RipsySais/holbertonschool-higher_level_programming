#!/usr/bin/python3
"""
This module defines a class Square.
ce mopdule defines a class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    Une classe Square qui hérite de Rectangle.
    """

    def __init__(self, size):
        """
        Initialize the square.
        Initialise le carré.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.
        Renvoie une représentation sous forme de chaîne du carré.
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
