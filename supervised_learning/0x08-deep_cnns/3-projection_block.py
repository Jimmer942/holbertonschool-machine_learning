#!/usr/bin/env python3
"""
a projection block.
"""

import tensorflow.keras as K


def projection_block(A_prev, filters, s=2):
    """the projection block of Deep Residual Learning for
    image Recognition
    """
    X = K.layers.Conv2D(filters=filters[0],
                        kernel_size=1,
                        padding='same',
                        strides=(s, s),
                        kernel_initializer='he_normal')(A_prev)

    X = K.layers.BatchNormalization(axis=3)(X)

    X = K.layers.Activation('relu')(X)

    X = K.layers.Conv2D(filters=filters[1],
                        kernel_size=3,
                        padding='same',
                        # strides=(s, s),
                        kernel_initializer='he_normal')(X)

    X = K.layers.BatchNormalization()(X)

    X = K.layers.Activation('relu')(X)

    X = K.layers.Conv2D(filters=filters[2],
                        kernel_size=1,
                        padding='same',
                        kernel_initializer='he_normal')(X)

    X = K.layers.BatchNormalization()(X)

    shortcut = K.layers.Conv2D(filters=filters[2],
                               kernel_size=1,
                               padding='same',
                               strides=(s, s),
                               kernel_initializer='he_normal')(A_prev)

    shortcut = K.layers.BatchNormalization()(shortcut)

    adding = K.layers.Add()([X, shortcut])

    output = K.layers.Activation('relu')(adding)

    return output
