#!/usr/bin/env python3
"""Train"""

import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False,
                patience=0, learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True, shuffle=False):
    """Train"""

    def step_decay(epoch):
        """Decay"""
        return alpha / (1 + decay_rate * epoch)

    callbacks = []

    if validation_data and learning_rate_decay:
        callbacks.append(K.callbacks.LearningRateScheduler(step_decay,
                                                           verbose=1))

    if validation_data and early_stopping:
        callbacks.append(K.callbacks.EarlyStopping(monitor="val_loss",
                                                   patience=patience))

    return network.fit(x=data,
                       y=labels,
                       batch_size=batch_size,
                       epochs=epochs,
                       verbose=verbose,
                       validation_data=validation_data,
                       shuffle=shuffle,
                       callbacks=callbacks)
