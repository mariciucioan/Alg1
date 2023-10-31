import random

import numpy as np


class OptimizationAlgorithm:
    def __init__(self, dimension, limits, function, n, precision, mode):
        self.dimension = dimension
        self.limits = limits
        self.function = function
        self.n = n
        self.precision = precision
        self.mode = mode

        self.bits_number = (limits[1] - limits[0]) * 10 ** precision
        self.bits_number = int(np.ceil(np.log2(self.bits_number)))

    def generate_candidate(self):
        result = ''.join([random.choice(['0', '1']) for _ in range(
            0, self.bits_number * self.dimension)])
        return result

    def evaluate(self, bitstring):
        parameters = []
        a = self.limits[0]
        b = self.limits[1]
        n = self.bits_number

        for i in range(0, self.dimension):
            parameter = int(bitstring[n * i: n * (i + 1)], 2)
            parameter = a + (parameter * (b - a) / (2 ** n - 1))
            parameters.append(parameter)

        return self.function(parameters)
