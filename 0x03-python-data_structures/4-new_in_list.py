#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        new_list = list.copy(my_list)
        return new_list
    elif idx >= len(my_list):
        new_list = list.copy(my_list)
        return new_list
    else:
        new_list = list.copy(my_list)
        new_list[idx] = element
        return new_list
