#!/usr/bin/env python3
"""Function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """
    INPUT: two matrix
    OUTPUT: A matrix containing the sum position by position
    """
    len(mat1[0])
    len(mat1)
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    new_ma = list()
    ar = list()
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            ar.append(mat1[i][j] + mat2[i][j])
        new_ma.append(ar)
        ar = []
    return new_ma
