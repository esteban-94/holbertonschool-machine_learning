#!/usr/bin/env python3
"""
This module concatenates two arrays
"""


def cat_arrays(arr1, arr2):
    """Function that do the work"""
    new_arr = arr1
    for idx_arr in range(len(arr2)):
        new_arr.append(arr2[idx_arr])
    return new_arr
