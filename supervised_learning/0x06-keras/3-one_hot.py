#!/usr/bin/env python3
"""Matrix"""
import tensorflow.keras as K


def one_hot(labels, classes=None):
    """Optimize"""

    return K.utils.to_categorical(labels, classes)
