#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list) > idx >= 0:
        new = my_list.copy()
        new[idx] = element
        return new
