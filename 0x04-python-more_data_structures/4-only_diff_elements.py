#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1_unique = set_1.difference(set_2)
    set_2_unique = set_2.difference(set_1)
    set_unique = set()
    for names in set_1_unique:
        set_unique.add(names)
    for names in set_2_unique:
        set_unique.add(names)
    return set_unique
