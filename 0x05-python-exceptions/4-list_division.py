#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    new_list = list(range(list_length))
    while (index < list_length):
        try:
            new_list[index] = my_list_1[index] / my_list_2[index]
        except (ValueError, TypeError):
            print("wrong type")
            new_list[index] = 0
        except ZeroDivisionError:
            print("division by 0")
            new_list[index] = 0
        except IndexError:
            print("out of range")
            new_list[index] = 0
        finally:
            index += 1
    return new_list
