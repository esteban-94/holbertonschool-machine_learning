#!/usr/bin/env python3
"""
This module add two matrices
"""

matrix_shape = __import__('2-size_me_please').matrix_shape


def add_matrices2D(matx1, matx2):
    """Function that do the work"""
    if matrix_shape(matx1) == matrix_shape(matx2):
        new_matx = []
        for idx_row in range(len(matx1)):
            new_matx.append([])
            for idx_column in range(len(matx1[0])):
                new_matx[idx_row].append(matx1[idx_row][idx_column]\
                + matx2[idx_row][idx_column])
        return new_matx
    else:
        return None
