#!/usr/bin/env python3
"""
This module performs element-wise addition, subtraction, multiplication
and division of two matrices
"""


def np_elementwise(mat1, mat2):
    """Function that do the work"""
    return (mat1.add(mat1, mat2),mat1.subtract(mat1, mat2)
            ,mat1.multiply(mat1, mat2),mat1.divide(mat1, mat2))
