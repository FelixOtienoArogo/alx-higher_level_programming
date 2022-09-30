#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    for i in a_dictionary:
        if a_dictionary[i] > a:
            a = a_dictionary[i]
    return i
