#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = str[i]
        sexy = ord(j)
        if (sexy >= 97 and sexy <= 122):
            j = chr(sexy - 32)
            print("{:j}".format(j), end="")
    print("")
