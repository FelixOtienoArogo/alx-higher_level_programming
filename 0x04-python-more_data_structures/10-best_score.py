#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    b = None
    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary[i] > a:
                a = a_dictionary[i]
                b = i
    return b
