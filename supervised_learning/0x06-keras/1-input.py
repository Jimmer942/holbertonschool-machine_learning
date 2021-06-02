#!/usr/bin/env python3
"""Sequential"""

import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """Sequential"""

    X = K.layers.Dense(layers[0],
                       activation=activations[0],
                       kernel_regularizer=K.regularizers.l2(lambtha))(X_input)

    for nodes, act in zip(layers[1::], activations[1::]):
        X = K.layers.Dropout(1 - keep_prob)(X)
        X = K.layers.Dense(nodes,
                           activation=act,
                           kernel_regularizer=K.regularizers.l2(lambtha))(X)

    model = K.Model(inputs=X_input, outputs=X)
    return model
