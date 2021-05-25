#!/usr/bin/env python3
"""Sensitivity"""

import numpy as np


def sensitivity(confusion):
    """Sensitivity"""

    true_positive = confusion.diagonal()
    positives = np.sum(confusion, axis=1).T
    return true_positive / positives
