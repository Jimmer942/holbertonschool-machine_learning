#!/usr/bin/env python3
""" INtegration """


def poly_integral(poly):
    """
    INPUT: polinom
    OUTPUT integration polinom
    """
    if poly == [] or type(poly) is not list:
        return None

    if type(poly[0]) is not int and type(poly[0]) is not float:
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
