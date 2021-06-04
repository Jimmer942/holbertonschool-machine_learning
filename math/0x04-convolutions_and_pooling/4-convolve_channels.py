#!/usr/bin/env python3
"""Channels"""

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    """Channels"""

    m, h, w, c = images.shape
    kh, kw, _ = kernel.shape
    sh, sw = stride

    if padding == 'same':
        ph = int(kh / 2)
        pw = int(kw / 2)

    elif padding == 'valid':
        ph, pw = (0, 0)

    elif padding is tuple and len(padding) == 2:
        ph, pw = padding

    padded_img = np.pad(images,
                        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                        'constant')

    ch = int((h + 2 * ph - kh) / sh) + 1
    cw = int((w + 2 * pw - kw) / sw) + 1

    convolved = np.zeros((m, ch, cw))

    for j in range(ch):
        for k in range(cw):
            images_slide = padded_img[:,
                                      j * sh:j * sh + kh,
                                      k * sw:k * sw + kw]

            elem_mul = np.multiply(images_slide, kernel)
            convolved[:, j, k] = elem_mul.sum(axis=1).sum(axis=1).\
                sum(axis=1)

    return convolved
