#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print(number, end=" ")
    print("is negative")
elif number == 0:
    print(number, end=" ")
    print("is zero")
elif number > 0:
    print(number, end=" ")
    print("is positive")
