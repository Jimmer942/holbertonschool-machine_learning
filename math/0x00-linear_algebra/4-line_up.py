#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None
    sum_arr = list()
    for i in range(len(arr1)):
        sum_arr.append(arr1[i] + arr2[i])
    return sum_arr