#!/usr/bin/env python3
"""
    Module Content:
        - A Poisson class that represent a poisson distribution.
"""


class Poisson:

    """
        Functions:
            - __init__(self, data=None, lambtha=1.): Class constructor
            - pmf(self, k): Calculate the value of the PMF for a given
                            number of "successes"
                    Returns: the PMF value of k
            - cdf(self, k): Calculate the value of the CDF for a given
                            number of "successes"
                    Returns: the CMF value of k
    """

    def __init__(self, data=None, lambtha=1.):
        """
            ___init__: class constructor

            @data: list of data to be used to estimate the distribution
            @lambtha: expected number of occurences in a given time frame

            Raises:
                ValueError: lambtha must be a positive value
                TypeError: data must be a list
                ValueError: data must contain multiple values
        """

        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pmf(self, k):
        """
            pmf: Calculates the value of the PMF for a given number of
            "successes"

            @k: the number of "successes"
            @e: Euler's number
            @fact: factorial number of k
            @lambtha: expected number of occurences in a given time frame


            Returns: the PMF value for k
        """

        e = 2.7182818285
        fact = 1
        lambtha = self.lambtha

        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        for i in range(1, k + 1):
            fact *= i
        return (lambtha ** k / (e ** lambtha * fact))

    def cdf(self, k):
        """
            cdf: Calculate the value of the CDF for a given number of
            "successes"

            @k: is the number of "successes"

            Return: the CDF value for k
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
