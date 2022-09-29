#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        a = []
        for j in i:
            a.append(j ** 2)
        new.append(a)
    return new
