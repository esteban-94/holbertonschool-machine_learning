#!/usr/bin/env python3
"""
This module concatenates two matrices in selected axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Function that do the work"""
    new_mat = []
    if (axis == 0 and len(mat1[0]) == len(mat2[0])) or (axis == 1 and len(mat1) == len(mat2)):
        if axis == 0:
            new_mat = [row[:] for row in mat1]
            for idx_row_mat2 in range(len(mat2)):
                new_mat.append([])
                for idx_column_mat2 in range(len(mat2[0])):
                    new_mat[len(new_mat)-1].append(mat2[idx_row_mat2][idx_column_mat2])
            return new_mat
        elif axis == 1:
            new_mat = [row[:] for row in mat1]
            for idx_row_mat1 in range(len(mat1)):
                for idx_row_mat2 in range(len(mat2[0])):
                    new_mat[idx_row_mat1].append(mat2[idx_row_mat1][idx_row_mat2])
            return new_mat
    else:
        return None
