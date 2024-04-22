#!/usr/bin/env python3
""" BayesianOptimization """

import numpy as np
from scipy.stats import norm
GP = __import__('2-gp').GaussianProcess


class BayesianOptimization:
    """
      Perform Bayesian optimization
      on a noiseless 1D Gaussian process
    """

    def __init__(self, f, X_init, Y_init, bounds, ac_samples, l=1, sigma_f=1,
                 xsi=0.01, minimize=True):
        """
          class constructor
        """
        self.f = f
        self.gp = GP(X_init, Y_init, l, sigma_f)
        X_s = np.linspace(bounds[0], bounds[1], num=ac_samples)
        self.X_s = X_s.reshape(-1, 1)
        self.xsi = xsi
        self.minimize = minimize

    def acquisition(self):
        """
          calculate the next best sample location
        """
        mu, sigma = self.gp.predict(self.X_s)
        if self.minimize is True:
            Y_sample = np.min(self.gp.Y)
            imp = Y_sample - mu - self.xsi
        else:
            Y_sample = np.max(self.gp.Y)
            imp = mu - Y_sample - self.xsi
        Z = np.zeros(sigma.shape[0])
        for i in range(sigma.shape[0]):
            if sigma[i] > 0:
                Z[i] = imp[i] / sigma[i]
            else:
                Z[i] = 0
            ei = imp * norm.cdf(Z) + sigma * norm.pdf(Z)
        X_next = self.X_s[np.argmax(ei)]
        return X_next, ei

    def optimize(self, iterations=100):
        """
          optimize the black-box function
        """
        X_all_s = []
        for i in range(iterations):
            x_opt, _ = self.acquisition()
            if x_opt in X_all_s:
                break
            y_opt = self.f(x_opt)
            self.gp.update(x_opt, y_opt)
            X_all_s.append(x_opt)
        if self.minimize is True:
            index = np.argmin(self.gp.Y)
        else:
            index = np.argmax(self.gp.Y)
        self.gp.X = self.gp.X[:-1]
        x_opt = self.gp.X[index]
        y_opt = self.gp.Y[index]
        return x_opt, y_opt
