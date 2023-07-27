#!/usr/bin/env python3
"""
This module performs element-wise addition, subtraction, multiplication
and division of two matrices
"""


def np_elementwise(mat1, mat2):
    """Function that do the work"""
    return (np.add(mat1, mat2),np.subtract(mat1, mat2)
            ,np.multiply(mat1, mat2),np.divide(mat1, mat2))
