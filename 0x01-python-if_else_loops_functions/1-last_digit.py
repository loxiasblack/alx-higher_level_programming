#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 > 5:
    print("Last digit of", end=" ")
    print(number, end=" ")
    print("is", end=" ")
    print(number % 10, end=" ")
    print("and is greater than 5")
elif number % 10 == 0:
    print("Last digit of", end=" ")
    print(number, end=" ")
    print("is", end=" ")
    print(number % 10, end=" ")
    print("and is 0")
elif (number % 10 < 6) and (number % 10 != 0):
    print("Last digit of", end=" ")
    print(number, end=" ")
    print("is", end=" ")
    print(number % 10, end=" ")
    print("and is less than 6 and not 0")
