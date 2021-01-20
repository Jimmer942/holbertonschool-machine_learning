#!/usr/bin/env python3
"""Function that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """
    INPUT: a matrix to transpose
    OUTPUT: the transpose matrix
    """
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
