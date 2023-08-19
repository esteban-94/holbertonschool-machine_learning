#!/usr/bin/env python3
"""
A Exponential class that represent an exponential distribution.
"""


class Exponential:

    """
        Functions:
            - def __init__(self, data=None, lambtha=1.): Class constructor
            - pmf(self, x): Calculate the value of the PMF for a given
                            number of "successes"
                    Returns: the PMF value of x
            - cdf(self, x): Calculate the value of the CDF for a given
                            number of "successes"
                    Returns: the CDF value of x
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
            self.lambtha = float(1 / (sum(data) / len(data)))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pdf(self, x):
        """
            pmf: Calculates the value of the PMF for a given number of
            "successes"

            @x: the number of "successes"
            @e: Euler's number
            @fact: factorial number of x
            @lambtha: expected number of occurences in a given time frame


            Returns: the PMF value for x
        """
        e = 2.7182818285
        lambtha = self.lambtha

        if x < 0:
            return 0
        return (lambtha * pow(e, (-lambtha * x)))

    def cdf(self, x):
        """
            cdf: Calculate the value of the CDF for a given number of
            "successes"

            @x: is the number of "successes"

            Return: the CDF value for x
        """
        e = 2.7182818285
        lambtha = self.lambtha

        if x < 0:
            return 0
        return (1 - pow(e, (-lambtha * x)))
