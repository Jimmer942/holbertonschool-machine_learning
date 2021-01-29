#!/usr/bin/env python3
""" INtegration """


def poly_integral(poly, C=0):
    """
    INPUT: polinom
    OUTPUT integration polinom
    """
    if poly == [] or type(poly) is not list or type(C) is not int:
        return None
    if type(poly[0]) is not int and type(poly[0]) is not float:
        return None
    if len(poly) == 1:
        if poly[0] == 0:
            return [C]
        else:
            return[C, poly[0]]

    inte = list()
    inte.append(C)

    for n in range(len(poly)):
        aux = poly[n] / (n + 1)
        if aux % 1 == 0:
            inte.append(int(aux))
        else:
            inte.append(aux)
    return inte
