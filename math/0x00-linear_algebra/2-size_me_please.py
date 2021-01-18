#!/usr/bin/env python3

def matrix_shape(matrix):
    m = list()
    arr = matrix[0]
    m.append(len(matrix))
    while type(arr) != int:
        m.append(len(arr))
        arr = arr[0]
    return m
