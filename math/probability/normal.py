#!/usr/bin/env python3
"""
- A Normal class that represents a normal distribution.
"""


class Normal:

    """
        Functions:
            - __init__: Class constructor
            - z_score(self, x): Calculates the z-score of a given x-value
                Return: the z-score of x
            - x_value(self, z): Calculates the x-value of a given z-score
            - pmf(self, x): Calculate the value of the PMF for a given
                            number of "successes"
            - cdf(self, x): Calculate the value of the CDF for a given
                            number of "successes"
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
            __init__: class constructor

            @data: list of the data to be used to estimate the distribution
            @mean: is the mean of the distribution
            @stddev: is the standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            sigma = 0
            for i in range(0, len(data)):
                x = pow((data[i] - self.mean), 2)
                sigma += x
            self.stddev = pow((sigma / len(data)), (1 / 2))

    def z_score(self, x):
        """
            z_score: Calculates the z-score of a given x-value

            @x: is the x-value

            Return: the z-score of x
        """
        return ((x - self.mean) / self.stddev)

    def x_value(self, z):
        """
            x_value: Calculates the x-value of a given z-score

            @z: is the z-score

            Return: the x-value of z
        """
        return ((z * self.stddev) + self.mean)

    def pdf(self, x):
        """
            pmf: Calculates the value of the PMF for a given number of
            "successes"

            @pi: Pi Value
            @e: Euler's number

            Returns: the PMF value for x
        """
        e = 2.7182818285
        pi = 3.1415926536
        mean = self.mean
        stddev = self.stddev
        return ((1 / (stddev * pow((2 * pi) ** (1 / 2)))) * e ** (
            (-1 / 2) * ((x - mean) / stddev) ** 2))

    def cdf(self, x):
        """
            cdf: Calculate the value of the CDF for a given number of
            "successes"

            @x: is the number of "successes"

            Return: the CDF value of x
        """
        pi = 3.1415926536
        z = (x - self.mean) / self.stddev
        ez = z / (2 ** (1 / 2))
        erf = (2 / (pi ** (1 / 2))) * (ez - ((ez ** 3) / 3) +
                                       ((ez ** 5) / 10) - ((ez ** 7) /
                                                           42) + ((ez ** 9)
                                                                  / 216))
        return ((1 / 2) * (1 + erf))
