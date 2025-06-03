#!/usr/bin/python3
"""Read a file and print its contents
to the standard output."""


def read_file(filename=""):
    """
    Read a file and print its contents
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
