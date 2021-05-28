#!/usr/bin/env python3
"""Early stopping"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """Early stopping"""

    if opt_cost - cost <= threshold:
        count += 1
    else:
        count = 0
    if count == patience:
        return (True, count)
    else:
        return (False, count)
