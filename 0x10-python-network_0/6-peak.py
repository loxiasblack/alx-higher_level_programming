#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers
    condition: algorithm must have the lowest complexity"""
    if not list_of_integers:
        return None
    start = 0
    end = len(list_of_integers) - 1

    while start < end:
        intsec = (start + end) // 2
        if list_of_integers[intsec + 1] < list_of_integers[intsec]:
            end = intsec
        else:
            start = intsec + 1

    return list_of_integers[start]
