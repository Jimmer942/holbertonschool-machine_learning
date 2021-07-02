#!/usr/bin/env python3
"""
an identity block
"""

import tensorflow.keras as K


def identity_block(A_prev, filters):
    """the identity block of Deep Residual Learning for
    Image Recognition
    """
    conv1 = K.layers.Conv2D(filters=filters[0],
                            kernel_size=1,
                            padding='same',
                            kernel_initializer='he_normal')(A_prev)

    batch1 = K.layers.BatchNormalization()(conv1)

    relu1 = K.layers.Activation('relu')(batch1)

    conv2 = K.layers.Conv2D(filters=filters[1],
                            kernel_size=3,
                            padding='same',
                            kernel_initializer='he_normal')(relu1)

    batch2 = K.layers.BatchNormalization()(conv2)

    relu2 = K.layers.Activation('relu')(batch2)

    conv3 = K.layers.Conv2D(filters=filters[2],
                            kernel_size=1,
                            padding='same',
                            kernel_initializer='he_normal')(relu2)

    batch3 = K.layers.BatchNormalization()(conv3)

    adding = K.layers.Add()([batch3, A_prev])

    output = K.layers.Activation('relu')(adding)

    return output
