#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    converted = 0
    for m, n in zip(roman_string, roman_string[1:]):
        if roman[m] < roman[n]:
            converted -= roman[m]
        else:
            converted += roman[m]
    converted += roman[roman_string[-1]]
    return converted
