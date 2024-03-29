#!/usr/bin/env python3
"""
a resnet
"""

import tensorflow.keras as K

identity_block = __import__('2-identity_block').identity_block
projection_block = __import__('3-projection_block').projection_block


def resnet50():
    """resNet-50 architecture of Deep Residual
    Learning for Image Recognition
    """
    X_input = K.layers.Input(shape=(224, 224, 3))

    # Stage 1: CONV-BN-ReLU-MAXPOOL
    X = K.layers.Conv2D(filters=64,
                        kernel_size=7,
                        strides=2,
                        padding='same',
                        kernel_initializer='he_normal')(X_input)
    X = K.layers.BatchNormalization(axis=3)(X)
    X = K.layers.Activation('relu')(X)
    X = K.layers.MaxPooling2D(pool_size=(3, 3),
                              padding='same',
                              strides=(2, 2))(X)

    X = projection_block(X, (64, 64, 256), 1)
    X = identity_block(X, (64, 64, 256))
    X = identity_block(X, (64, 64, 256))

    X = projection_block(X, (128, 128, 512))
    X = identity_block(X, (128, 128, 512))
    X = identity_block(X, (128, 128, 512))
    X = identity_block(X, (128, 128, 512))

    X = projection_block(X, (256, 256, 1024))
    X = identity_block(X, (256, 256, 1024))
    X = identity_block(X, (256, 256, 1024))
    X = identity_block(X, (256, 256, 1024))
    X = identity_block(X, (256, 256, 1024))
    X = identity_block(X, (256, 256, 1024))

    X = projection_block(X, (512, 512, 2048))
    X = identity_block(X, (512, 512, 2048))
    X = identity_block(X, (512, 512, 2048))

    X = K.layers.AvgPool2D(pool_size=(7, 7),
                           padding='same')(X)

    X = K.layers.Dense(units=1000,
                       activation='softmax',
                       kernel_initializer='he_normal')(X)

    model = K.Model(inputs=X_input, outputs=X)

    return model
