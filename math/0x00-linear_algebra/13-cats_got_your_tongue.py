#!/usr/bin/env python3
"""
function def np_cat(mat1, mat2, axis=0)
that concatenates two matrices along a specific axis
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    INPUT: Two matrix
    OUTPUT: the matrix's concat
    """
    return np.concatenate((mat1, mat2), axis=axis)
