#!/usr/bin/env python3
"""L2 Regularization"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """L2 Regularization"""

    suma = 0
    for l in range(1, L + 1):
        key = "W{}".format(l)
        suma += np.linalg.norm(weights[key])

    L2_cost = lambtha * suma / (2 * m)

    return cost + L2_cost
