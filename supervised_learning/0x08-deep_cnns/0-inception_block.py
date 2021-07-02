#!/usr/bin/env python3
"""
the inception block.
"""

import tensorflow.keras as K


def inception_block(A_prev, filters):
    """the inception block of Going Deeper with
    Convolutions .
    """
    O1 = K.layers.Conv2D(filters=filters[0],
                         kernel_size=1,
                         padding='same',
                         kernel_initializer='he_normal',
                         activation='relu')(A_prev)

    O3R = K.layers.Conv2D(filters=filters[1],
                          kernel_size=1,
                          padding='same',
                          kernel_initializer='he_normal',
                          activation='relu')(A_prev)

    OFPPR = K.layers.MaxPooling2D(pool_size=(3, 3),
                                  padding='same',
                                  strides=(1, 1))(A_prev)

    O3 = K.layers.Conv2D(filters=filters[2],
                         kernel_size=3,
                         padding='same',
                         kernel_initializer='he_normal',
                         activation='relu')(O3R)

    O5R = K.layers.Conv2D(filters=filters[3],
                          kernel_size=1,
                          padding='same',
                          kernel_initializer='he_normal',
                          activation='relu')(A_prev)

    O5 = K.layers.Conv2D(filters=filters[4],
                         kernel_size=5,
                         padding='same',
                         kernel_initializer='he_normal',
                         activation='relu')(O5R)

    OFPP = K.layers.Conv2D(filters=filters[5],
                           kernel_size=1,
                           padding='same',
                           kernel_initializer='he_normal',
                           activation='relu')(OFPPR)

    concatenate_filters = K.layers.Concatenate(axis=3)([O1, O3, O5, OFPP])

    return concatenate_filters
