#!/usr/bin/env python3
"""Normalization"""

import numpy as np


def normalization_constants(X):
    """Returns the mean ans standar deviation"""
    m = np.mean(X, axis=0)
    s = np.std(X, axis=0)
    return m, s
