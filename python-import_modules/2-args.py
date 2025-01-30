#!/usr/bin/python3
import sys

if __name__ == "__main__":
    numargs = len(sys.argv) - 1
    if numargs == 0:
        print("0 arguments.")
    elif numargs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numargs))
    for i in range(numargs):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
