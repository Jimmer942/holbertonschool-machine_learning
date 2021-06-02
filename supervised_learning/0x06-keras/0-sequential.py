#!/usr/bin/env python3
"""Sequential"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Sequential"""

    model = K.models.Sequential()
    model.add(K.layers.Dense(layers[0],
                             input_dim=nx,
                             activation=activations[0],
                             kernel_regularizer=K.regularizers.l2(lambtha)))
    for nodes, act in zip(layers[1::], activations[1::]):
        model.add(K.layers.Dropout(1 - keep_prob))
        model.add(K.layers.
                  Dense(nodes,
                        activation=act,
                        kernel_regularizer=K.regularizers.l2(lambtha)))

    return model
