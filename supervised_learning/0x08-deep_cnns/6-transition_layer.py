#!/usr/bin/env python3
"""
a dense Block
"""

import tensorflow.keras as K


def transition_layer(X, nb_filters, compression):
    """builds a transition layer of Densely Connected
    Convolutional Networks
    """
    nb_filters = int(nb_filters * compression)

    x = K.layers.BatchNormalization()(X)
    x = K.layers.Activation('relu')(x)
    x = K.layers.Conv2D(filters=nb_filters,
                        kernel_size=1,
                        padding='same',
                        kernel_initializer='he_normal')(x)

    x = K.layers.AvgPool2D(pool_size=(2, 2),
                           strides=(2, 2),
                           padding='valid')(x)

    return x, nb_filters
