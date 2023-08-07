#!/usr/bin/env python3
"""
Calculate the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculate the integral of a polynomial
    """
    if not isinstance(poly, list) or len(poly) < 1:
        return None

    if not isinstance(C, (int, float)):
        return None

    if poly == [0]:
        return [C]

    integral = [C]

    for pwd, coe in enumerate(poly):
        # Check if the coefficient is a number.
        if not isinstance(coe, (int, float)):
            return None

        # Check if the integral is an integer.
        if coe / (pwd + 1) % 1 == 0:
            integral.append(int(coe / (pwd + 1)))
        else:
            integral.append(coe / (pwd + 1))

    # Remove any trailing zeros from the integral
    while len(integral) > 1 and integral[-1] == 0:
        integral.pop()

    return integral
