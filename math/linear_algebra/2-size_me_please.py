#!/usr/bin/env python3
"""
This module calculate a shape of a matrix
"""
def matrix_shape(matx):
    grade = 0
    for bracket in str(matx):
        if bracket == '[':
            grade += 1
        else:
            break

    matx_leng = []
    matx_index = "matx"
    for count in range(grade):
        matx_leng.append(len(eval(matx_index)))
        matx_index += "[0]"
    return matx_leng
