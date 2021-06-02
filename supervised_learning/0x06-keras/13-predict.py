#!/usr/bin/env python3
"""Prediction"""

import tensorflow.keras as K


def predict(network, data, verbose=False):
    """Prediction"""

    return network.predict(data, verbose=verbose)
