#!/usr/bin/env python3
"""Function def mat_mul(mat1, mat2): that performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """
    INPUT: two matrix
    OUTPUT: the matrix multiplication
    """
    if len(mat1[0]) != len(mat2):
        return None

    new_m = [[0 for x in range(len(mat2[0]))] for y in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                new_m[i][j] += mat1[i][k] * mat2[k][j]
    return new_m
