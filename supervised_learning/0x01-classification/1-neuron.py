#!/usr/bin/env python3
import numpy as np


class Neuron():
    def __init__(self, nx):

        if type(nx) is not int:
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        self.nx = nx
        self.__W = np.random.randn(nx).reshape(1, nx)
        self.__b = 0
        self.__A = 0

        @property
        def W():
            return self.__W

        @property
        def b():
            return self.__b

        @property
        def A():
            return self.__A
