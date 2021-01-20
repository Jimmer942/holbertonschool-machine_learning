#!/usr/bin/env python3
"""Function def add_arrays(arr1, arr2): that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """
    INPUT: two arrays
    OUTPUT: An array containing the sum position by position
    """
    if len(arr1) != len(arr2):
        return None
    sum_arr = list()
    for i in range(len(arr1)):
        sum_arr.append(arr1[i] + arr2[i])
    return sum_arr
