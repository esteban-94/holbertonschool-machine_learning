#!/usr/bin/env python3
"""
Calculate the sum of squares from 1 to n.
"""


def summation_i_squared(n):
    """
    Calculate the sum of squares from 1 to n.
    """
    if n > 0:
        return int(n * (n + 1) * (2 * n + 1) / 6)
    return None
