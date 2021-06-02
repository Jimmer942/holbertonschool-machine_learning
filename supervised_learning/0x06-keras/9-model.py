#!/usr/bin/env python3
"""Models"""

import tensorflow.keras as K


def save_model(network, filename):
    """Models"""

    network.save(filename)
    return None


def load_model(filename):
    """Models"""
    return K.models.load_model(filename)
