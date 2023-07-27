#!/usr/bin/env python3
"""
This module performs element-wise addition, subtraction, multiplication
and division of two matrices
"""


def np_elementwise(mat1, mat2):
    """Function that do the work"""
    return (add(mat1, mat2),subtract(mat1, mat2)
            ,multiply(mat1, mat2),divide(mat1, mat2))
