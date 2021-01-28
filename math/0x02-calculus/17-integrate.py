#!/usr/bin/env python3
""" INtegration """


def poly_integral(poly, C=0):
    """
    INPUT: polinom
    OUTPUT integration polinom
    """
    if poly == [] or type(poly) is not list:
        return None

    if poly == [] or type(poly) is not list or type(C) is not int:
        return None

    inte = list()
    inte.append(C)

    if len(poly) == 1:
        return [C]

    for n in range(len(poly)):
        aux = poly[n] / (n + 1)
        if aux % 1 == 0:
            inte.append(int(aux))
        else:
            inte.append(aux)
    return inte
