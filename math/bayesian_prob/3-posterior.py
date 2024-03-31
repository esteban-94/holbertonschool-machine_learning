#!/usr/bin/env python3
"""Posterior Probability"""

import numpy as np
intersection = __import__('1-intersection').intersection
marginal = __import__('2-marginal').marginal


def posterior(x, n, P, Pr):
    """
      Calculate the posterior probability for the various
      hypothetical probabilities.
    """
    return intersection(x, n, P, Pr) / marginal(x, n, P, Pr)
