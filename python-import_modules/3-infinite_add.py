#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num = len(sys.argv) - 1
    num_total = 0
    for i in range(num):
        num_total += int(sys.argv[i + 1])
print(num_total)
