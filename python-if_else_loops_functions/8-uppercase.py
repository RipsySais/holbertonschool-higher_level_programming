#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if ord('A') <= ord(char) <= ord('Z'):
            result += chr(ord(char) - 32)
        else:
            result += char
            print("{}".format(result))
