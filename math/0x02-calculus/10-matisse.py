#!/usr/bin/env python3
""" Derivation """


def poly_derivative(poly):
    """
    INPUT: polinom
    OUTPUT d(polinom)/dx
    """
    if poly == [] or type(poly) is not list:
        return None

    if type(poly[0]) is not int and type(poly[0]) is not float:
        return None

    der = list()

    if len(poly) == 1:
        return [0]

    for n in range(1, len(poly)):
        der.append(poly[n] * n)

    return der
