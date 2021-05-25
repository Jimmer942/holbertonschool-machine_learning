#!/usr/bin/env python3
"""Score"""

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """Score"""

    PPV = precision(confusion)
    TPR = sensitivity(confusion)
    return 2 * PPV * TPR / (PPV + TPR)
