#!/usr/bin/env python3
"""
This module concatenates two matrices along a specific axis
"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Function that do the work"""
    return np.concatenate((mat1, mat2), axis)
