#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for i, j in new_dic.items():
        new_dic[i] = j * 2
    return new_dic
