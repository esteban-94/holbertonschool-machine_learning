#!/usr/bin/env python3
"""
This module multiplies two matrices
"""


def mat_mul(mat1, mat2):
    """Function that do the work"""
    if len(mat1[0]) == len(mat2):
        new_mat = []
        for idx_row_mat1 in range(len(mat1)):
            new_mat.append([])
            for idx_column_mat2 in range(len(mat2[0])):
                product = 0
                for idx_column_mat1 in range(len(mat1[0])):
                    product += (mat1[idx_row_mat1][idx_column_mat1] *
                                mat2[idx_column_mat1][idx_column_mat2])
                new_mat[len(new_mat)-1].append(product)
        return new_mat
    else:
        return None
