#!/usr/bin/python3
"""
This module defines a class Rectangle that inherits from BaseGeometry.
ce module définit une classe Rectangle qui hérite de BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    Une classe Rectangle qui hérite de BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize the rectangle.
        Initialise le rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        Calcule l'aire du rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.
        Renvoie une représentation sous forme de chaîne du rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
