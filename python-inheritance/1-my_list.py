#!/usr/bin/python3
""""Module that defines a class MyList that"""
"""module qui définit une classe MyList qui hérite de list"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
