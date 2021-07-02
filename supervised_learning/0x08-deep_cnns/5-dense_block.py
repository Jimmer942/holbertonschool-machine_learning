#!/usr/bin/env python3
"""
a dense Block
"""

import tensorflow.keras as K


def bottlenecks(inputs, growth_rate):
    """checks bottlenecks layers
    """
    x = K.layers.BatchNormalization()(inputs)
    x = K.layers.Activation('relu')(x)
    x = K.layers.Conv2D(filters=4 * growth_rate,
                        kernel_size=1,
                        padding='same',
                        kernel_initializer='he_normal')(x)

    x = K.layers.BatchNormalization()(x)
    x = K.layers.Activation('relu')(x)
    x = K.layers.Conv2D(filters=growth_rate,
                        kernel_size=(3, 3),
                        padding='same',
                        kernel_initializer='he_normal')(x)
    return x


def dense_block(X, nb_filters, growth_rate, layers):
    """dense block of Densely Connected Convolutional
    Networks
    """
    for i in range(layers):
        conv_outputs = bottlenecks(X, growth_rate)
        X = K.layers.concatenate([X, conv_outputs])
        nb_filters += growth_rate

    return X, nb_filters
