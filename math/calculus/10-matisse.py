#!/usr/bin/env python3
"""
Calculate the derivative of a polynomial
"""


def poly_derivative(poly):
    """
        Calculate the derivative of a polynomial
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    derivative = []
    for i in range(1, len(poly)):
        if type(poly[i]) is not int:
            return None
        derivative.append(poly[i] * (i))

    return derivative
