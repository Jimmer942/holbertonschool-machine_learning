#!/usr/bin/env python3
"""
Function def np_elementwise(mat1, mat2):
that performs element-wise addition, subtraction, multiplication, and division
"""


def np_elementwise(mat1, mat2):
    """
    INPUT: Two matrix
    OUTPUT: the matrix's transpose
    """
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
