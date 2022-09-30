#!/usr/bin/python3
def search_replace(my_list, search, replace):
    j = 0
    new = my_list.copy()
    for i in new:
        if i == search:
            new[j] = replace
        j += 1
    return new
