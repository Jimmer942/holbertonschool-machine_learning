#!/usr/bin/env python3

def matrix_transpose(matrix):
    ind = 0
    new_m = list()
    ar = list()
    while ind < len(matrix[0]):
        for i in matrix:
            ar.append(i[ind])
        new_m.append(ar)
        ar = []
        ind += 1
    return new_m
