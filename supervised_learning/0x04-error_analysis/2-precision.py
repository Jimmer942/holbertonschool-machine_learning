#!/usr/bin/env python3
"""Precision"""

import numpy as np


def precision(confusion):
    """Precision"""

    true_positive = confusion.diagonal()
    TP_FP = np.sum(confusion, axis=0)
    return true_positive / TP_FP
