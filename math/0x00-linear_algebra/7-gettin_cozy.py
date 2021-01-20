#!/usr/bin/env python3
"""Function that concatenates two matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    INPUT: two matrix
    OUTPUT: the matrix concat horizontally with axis = 0 or vertically
    """

    new_m = []
    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        for i in range(len(mat2)):
            new_m.append(mat1[i] + mat2[i])
    elif axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        new_m = [[n for n in row] for row in mat1]
        for i in mat2:
            new_m.append(i)
    return new_m
