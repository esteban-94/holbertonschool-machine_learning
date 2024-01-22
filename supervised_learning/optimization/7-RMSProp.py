#!/usr/bin/env python3
"""
module update_variables_RMSProp
"""
import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
    updates a variable using the RMSProp optimization algorithm
    """
    s = beta2 * s + (1 - beta2) * (grad ** 2)
    updt = var - alpha * grad / (s ** (1/2) + epsilon)
    return updt, s
