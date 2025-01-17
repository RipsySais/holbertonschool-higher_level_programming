#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number} est positif")
elif number == 0:
    print(f"{number} est nul")
elif number < 0:
    print(f"{number} est négatif")
