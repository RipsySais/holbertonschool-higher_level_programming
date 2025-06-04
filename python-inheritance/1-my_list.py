#!/usr/bin/python3

"""Module that defines a class MyList that inherits from list"""


class MyList(list):
    """Class that defines a list"""

    def print_sorted(self):
        """Prints the list sorted"""
        print(sorted(self))
        