#!/usr/bin/env python3
"""Pooling"""

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """Pooling"""

    m, h, w, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    poolh = int((h - kh) / sh) + 1
    poolw = int((w - kw) / sw) + 1

    pooled = np.zeros((m, poolh, poolw, c))

    for j in range(poolh):
        for k in range(poolw):
            images_slide = images[:,
                                  j * sh:j * sh + kh,
                                  k * sw:k * sw + kw]
            if mode == 'max':
                pooled[:, j, k] = np.max(images_slide, axis=1).max(axis=1)
            elif mode == 'avg':
                pooled[:, j, k] = np.mean(images_slide, axis=1).mean(axis=1)

    return pooled
