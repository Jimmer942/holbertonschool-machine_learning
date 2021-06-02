#!/usr/bin/env python3
"""Weights"""

import tensorflow.keras as K


def save_weights(network, filename, save_format='h5'):
    """Weights"""

    network.save_weights(filename, save_format=save_format)
    return None


def load_weights(network, filename):
    """Weights"""

    network.load_weights(filename)
