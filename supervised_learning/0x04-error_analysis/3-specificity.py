#!/usr/bin/env python3
"""Specificity"""

import numpy as np


def specificity(confusion):
    """Specificity"""

    classes = confusion.shape[0]
    total = np.array([np.sum(confusion)] * classes)
    FN = np.sum(confusion, axis=0)
    FP = np.sum(confusion, axis=1)
    TP = confusion.diagonal()
    TN = total - FN - FP + TP
    FP = FN - TP

    return TN / (TN + FP)
