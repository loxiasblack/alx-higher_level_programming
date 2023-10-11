#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    result = 0
    for i in range(len(my_list)):
        if my_list[i] != my_list[i - 1]:
            result += my_list[i]
    return result
