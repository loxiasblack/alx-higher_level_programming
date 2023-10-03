#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = (abs(number) % 10) * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print("Last digit of", end=" ")
    print(number, end=" ")
    print("is", end=" ")
    print(last_digit, end=" ")
    print("and is greater than 5")
elif last_digit == 0:
    print("Last digit of", end=" ")
    print(number, end=" ")
    print("is", end=" ")
    print(last_digit, end=" ")
    print("and is 0")
elif (number % 10 < 6) and (number % 10 != 0):
    print("Last digit of", end=" ")
    print(number, end=" ")
    print("is", end=" ")
    print(last_digit, end=" ")
    print("and is less than 6 and not 0")
