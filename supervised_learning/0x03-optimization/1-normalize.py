#!/usr/bin/env python3
"""Normalization"""

import numpy as np


def normalize(X, m, s):
    """Returns a normalize matrix"""
    return (X - m)/s
