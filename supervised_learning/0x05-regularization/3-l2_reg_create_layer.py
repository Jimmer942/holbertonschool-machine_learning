#!/usr/bin/env python3
"""L2 Regularization"""

import tensorflow as tf


def l2_reg_create_layer(prev, n, activation, lambtha):
    """L2 Regularization """

    reg = tf.contrib.layers.l2_regularizer(lambtha)
    init = tf.contrib.layers.variance_scaling_initializer(mode="FAN_AVG")
    layer = tf.layers.Dense(units=n, activation=activation,
                            kernel_initializer=init, kernel_regularizer=reg)
    return layer(prev)
