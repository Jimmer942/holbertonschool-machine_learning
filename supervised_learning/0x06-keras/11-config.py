#!/usr/bin/env python3
"""Config"""

import tensorflow.keras as K


def save_config(network, filename):
    """Config"""

    model_json = network.to_json()
    with open(filename, "w") as json_file:
        json_file.write(model_json)


def load_config(filename):
    """Config"""

    with open(filename, "r") as json_file:
        loaded_model_json = json_file.read()

    loaded_model = K.models.model_from_json(loaded_model_json)

    return loaded_model
