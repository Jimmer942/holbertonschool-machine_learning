#!/usr/bin/env python3
"""Valid"""

import numpy as np


def convolve_grayscale_valid(images, kernel):
    """Valid"""

    m, h, w = images.shape
    kh, kw = kernel.shape

    ch = h - kh + 1
    cw = w - kw + 1
    convolved = np.zeros((m, ch, cw))

    for j in range(ch):
        for k in range(cw):
            images_slide = images[:, j:j + kh, k:k + kw]
            elem_mul = np.multiply(images_slide, kernel)
            convolved[:, j, k] = elem_mul.sum(axis=1).sum(axis=1)

    return convolved
