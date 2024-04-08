#!/usr/bin/env python3
""" Module Initialize Clustering"""

import numpy as np


def initialize(X, k):
    """
      Initialize cluster centroids for K-means.
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None
    if not isinstance(k, int) or k <= 0:
        return None
    n, d = X.shape
    X_min = X.min(axis=0)
    X_max = X.max(axis=0)
    return np.random.uniform(X_min, X_max, size=(k, d))
