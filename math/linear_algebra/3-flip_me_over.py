#!/usr/bin/env python3
"""
This module genreate a new transpose matrix
"""


def matrix_transpose(matx):
    """Function that do the work"""
    new_matx = []
    for idx in matx[0]:
        new_matx.append([])

    for row in range(len(matx)):
        for column in range(len(matx[0])):
            new_matx[column].append(matx[row][column])
    return new_matx
