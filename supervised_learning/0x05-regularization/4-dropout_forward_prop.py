#!/usr/bin/env python3
"""DropOut Regularization"""

import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    """DropOut Regularization"""

    cache = {}
    cache['A0'] = X

    for la in range(1, L + 1):
        keyA = "A{}".format(la)
        keyA_p = "A{}".format(la - 1)
        keyD = "D{}".format(la)
        keyW = "W{}".format(la)
        keyb = "b{}".format(la)

        Z = np.matmul(weights[keyW], cache[keyA_p]) + weights[keyb]

        if la != L:
            A = (np.exp(Z) - np.exp(-Z)) / (np.exp(Z) + np.exp(-Z))
            D = np.random.rand(A.shape[0], A.shape[1])
            D = np.where(D < keep_prob, 1, 0)
            cache[keyD] = D
            A *= D
            A /= keep_prob
            cache[keyA] = A
        else:
            t = np.exp(Z)
            A = t / np.sum(t, axis=0, keepdims=True)
            cache[keyA] = A

    return cache
