#!/usr/bin/python3

class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
