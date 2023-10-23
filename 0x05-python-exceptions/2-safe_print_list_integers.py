#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        i = 0
        y = 0
        while i < x:
            if type(my_list[i]) is int:
                y += 1
                print("{:d}".format(my_list[i]), end="")
            i += 1
        print()
        return y
    except (IndexError):
        raise IndexError("list index out of range")
