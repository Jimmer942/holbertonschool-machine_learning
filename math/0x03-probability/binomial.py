#!/usr/bin/env python3
"""Binomial"""


e = 2.7182818285
pi = 3.1415926536


def factorial(n):
    """Calculates factorial of integer"""
    ans = 1
    if n == 0:
        return 1

    for n in range(1, n + 1):
        ans *= n

    return ans


class Binomial():
    """* Binomial"""

    def __init__(self, data=None, n=1, p=0.5):
        """Initializes the distribution """
        self.n = int(n)
        self.p = float(p)

        if data is None:
            if self.n < 1:
                raise ValueError("n must be a positive value")
            elif self.p <= 0 or self.p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")

        else:
            if isinstance(data, list):
                if len(data) > 1:
                    self.data = data
                    mean = sum(self.data) / len(self.data)
                    variance = (sum([(num - mean) ** 2 for num in self.data]) /
                                len(self.data))
                    p = 1 - variance / mean
                    self.n = int(round(mean / p))
                    self.p = mean / self.n
                else:
                    raise ValueError("data must contain multiple values")

            else:
                raise TypeError("data must be a list")

    def pmf(self, k):
        """ Calculates the pmf at a given k"""
        x = int(k)
        if x > self.n or x < 0:
            return 0
        else:
            n = int(self.n)
            combination = factorial(n) / (factorial(x) * factorial(n - x))
            probability = (self.p ** x) * ((1 - self.p) ** (n - x))
            return combination * probability

    def cdf(self, k):
        """ Calculates the cdf """
        x = int(k)
        if x > self.n or x < 0:
            return 0

        cdf = 0
        for i in range(x + 1):
            cdf += self.pmf(i)
        return cdf
