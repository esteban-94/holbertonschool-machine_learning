#!/usr/bin/env python3
""" Module documentation """

import numpy as np


def normalization_constants(X):
    """
        Calculates the normalization
        (standardization) constants of a matrix

        Return: the mean and standard deviation of
        each feature, respectively
    """
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)

    return mean, std
