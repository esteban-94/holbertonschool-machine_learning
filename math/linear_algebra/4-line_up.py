#!/usr/bin/env python3
"""
This module add two arrays
"""

matrix_shape = __import__('2-size_me_please').matrix_shape


def add_arrays(matx1, matx2):
    """Function that do the work"""
    if matrix_shape(matx1) == matrix_shape(matx2):
        new_matx = []
        for idx in range(len(matx1)):
            new_matx.append(matx1[idx] + matx2[idx])
        return new_matx
    else:
        return None
