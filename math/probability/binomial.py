#!/usr/bin/env python3
"""
- A Binomial class that represent a binomial distribution
"""


class Binomial:

    """
        Functions:
            - __init__: Class constructor
            - def pmf(self, k): Calculate the value of the PMF for a given
                            number of "successes"
            - def cdf(self, k): Calculate the value of the CDF for a given
                            number of "successes"
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
            __init__: Class constructor

            @data: list of the data to be used to estimate the distribution
            @n: number of Bernoulli trials
            @p: probability of a "successes"
        """
        self.n = int(n)
        self.p = float(p)
        if data is None:
            if self.n < 1:
                raise ValueError("n must be a positive value")
            elif self.p <= 0 or self.p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)

            variance = 0
            for idx in range(len(data)):
                variance += pow((data[idx] - mean), 2)
            variance = variance / len(data)

            self.p = 1 - (variance / mean)
            self.n = int(round(mean / self.p))
            self.p = mean / self.n

    def pmf(self, k):
        """
            pmf: Calculates the value of the PMF for a given number of
            "successes"

            Returns: the PMF value for k
        """
        k = int(k)
        factor_k = 1
        factor_n = 1
        factor_c = 1

        if k > self.n or k < 0:
            return 0

        for num in range(1, k + 1):
            factor_k *= num
        for num in range(1, self.n + 1):
            factor_n *= num
        for num in range(1, (self.n - k) + 1):
            factor_c *= num

        comb = factor_n / (factor_c * factor_k)
        prob = pow(self.p, k) * pow((1 - self.p), (self.n - k))
        return comb * prob

    def cdf(self, k):
        """
            cdf: Calculates the value of the CDFfor a given number
            of “successes”

            Return the CDF value of k
        """

        k = int(k)
        if k < 0:
            return 0

        cdf = sum(self.pmf(i) for i in range(k + 1))
        return cdf
