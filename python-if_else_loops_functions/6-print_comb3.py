#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i != 0 or j != 1:
            print(f"{i:02}, {j:02}", end=", ")
        else:
            print(f"{i:02}, {j:02}")
