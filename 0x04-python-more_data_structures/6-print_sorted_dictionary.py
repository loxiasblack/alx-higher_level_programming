#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_sorted = sorted(a_dictionary.items())
    for i, j in dict_sorted:
        print("{:s}: {}".format(i, j))
