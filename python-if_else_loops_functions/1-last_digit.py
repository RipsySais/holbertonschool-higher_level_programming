#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10 if number >= 0 else -abs(number) % 10 

print(f"Dernier chiffre de {number} est {last_digit} et", end=" ")

if last_digit > 5:
    print("est supérieur à 5")
elif last_digit == 0:
    print("est 0")
else:
    print ("est inférieur à 6 et non à 0")
