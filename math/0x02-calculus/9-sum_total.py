#!/usr/bin/env python3
"""Sigma square"""


def summation_i_squared(n):
    """
    INPUT limit for sumatory
    OUTPUT sumatory i**2, from i = 1 to i = n
    """
    if n < 1 or type(n) is not int or n is None:
        return None
    else:
        return int(n * (n + 1) * (2 * n + 1) / 6)
