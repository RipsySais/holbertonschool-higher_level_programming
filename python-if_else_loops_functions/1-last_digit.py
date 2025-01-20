#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
elif number < 0:
    last_digit = ((number * -1) % 10) * -1
if last_digit > 5:
    str = 'last digit de {0} est {1} et est supérieur à 5'
elif last_digit < 6 and last_digit != 0:
    str = 'last digit de {0} est {1} et est inféreur à 6 non à 0'
elif last_digit == 0:
    str = 'last digit de {0} est {1} et et est {0}'
print(str.format(number, last_digit))
