#!/usr/bin/env python3
""" Module Viterbi """

import numpy as np


def viterbi(Observation, Emission, Transition, Initial):
    """
      Calculate the most likely sequence of hidden
      states for a hidden markov model.
    """
    try:
        T = Observation.shape[0]
        N, M = Emission.shape
        backpointer = np.zeros((N, T))
        F = np.zeros((N, T))
        F[:, 0] = Initial.T * Emission[:, Observation[0]]
        for t in range(1, T):
            for n in range(N):
                Transitions = Transition[:, n]
                Emissions = Emission[n, Observation[t]]
                F[n, t] = np.amax(Transitions * F[:, t - 1] * Emissions)
                backpointer[n, t - 1] = np.argmax(Transitions * F[:, t - 1] *
                                                  Emissions)
        path = [0 for i in range(T)]
        last_state = np.argmax(F[:, T - 1])
        path[0] = last_state
        backtrack_index = 1
        for i in range(T - 2, -1, -1):
            path[backtrack_index] = int(backpointer[int(last_state), i])
            last_state = backpointer[int(last_state), i]
            backtrack_index += 1
        path.reverse()
        P = np.amax(F[:, T - 1], axis=0)
        return path, P
    except Exception:
        None, None
