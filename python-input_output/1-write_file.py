#!/usr/bash/python3
def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
