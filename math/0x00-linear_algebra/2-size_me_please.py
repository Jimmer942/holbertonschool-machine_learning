#!/usr/bin/env python3
"""function def matrix_shape(matrix): that calculates the shape of a matrix:"""

def matrix_shape(matrix):
    m = list()
    arr = matrix[0]
    m.append(len(matrix))
    while type(arr) != int:
        m.append(len(arr))
        arr = arr[0]
    return m
