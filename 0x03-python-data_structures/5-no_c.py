#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    for i in range(len(new_list)):
        if new_list[i] == "C" or new_list[i] == "c":
            new_list[i] = ""
    return "".join(new_list)
