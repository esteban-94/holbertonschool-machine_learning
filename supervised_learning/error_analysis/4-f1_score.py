#!/usr/bin/env python3
"""
module f1_score
"""
import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """
    calculates the F1 score of a confusion matrix
    """
    prec = precision(confusion)
    recall = sensitivity(confusion)
    f1 = 2 * (prec * recall) / (prec + recall)
    return f1
