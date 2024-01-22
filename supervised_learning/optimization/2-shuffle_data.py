#!/usr/bin/env python3
""" Module documentation """

import numpy as np


def shuffle_data(X, Y):
    """shuffles the data points in two
    matrices the same way"""

    shuffled_indices = np.random.permutation(X.shape[0])

    X_shuffled = X[shuffled_indices, :]
    Y_shuffled = Y[shuffled_indices, :]

    return X_shuffled, Y_shuffled
