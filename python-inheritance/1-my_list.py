#!/usr/bin/python3
"""
Module that defines a class MyList that inherits from list
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        sorted_list = sorted(self)
        print(sorted_list)
