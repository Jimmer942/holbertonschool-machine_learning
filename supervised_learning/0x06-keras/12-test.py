#!/usr/bin/env python3
"""Test"""

import tensorflow.keras as K


def test_model(network, data, labels, verbose=True):
    """Test"""

    return network.evaluate(data, labels, verbose=verbose)
