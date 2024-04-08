#!/usr/bin/env python3
""" Module: Variance """

import numpy as np


def variance(X, C):
    """
      Calculate the total intra-cluster variance.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None
    if not isinstance(C, np.ndarray) or len(C.shape) != 2:
        return None
    if X.shape[1] != C.shape[1]:
        return None
    n, d = X.shape
    centroids_extended = C[:, np.newaxis]
    distances = np.sqrt(((X - centroids_extended) ** 2).sum(axis=2))
    min_distances = np.min(distances, axis=0)
    variance = np.sum(min_distances ** 2)
    return variance
