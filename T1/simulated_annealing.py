import numpy as np
import random


def swap_bit(bitstring, bit_pos):
    result = ''
    for i in range(0, len(bitstring)):
        if i == bit_pos:
            result += str(-1 * (int(bitstring[i]) - 1))
        else:
            result += bitstring[i]

    return result


def mutation(bitstring):
    mutation_bit = random.randint(0, len(bitstring) - 1)
    return swap_bit(bitstring, mutation_bit)


class SimulatedAnnealing:
    def __init__(self, dimension, limits, function, n=200, precision=3):
        self.dimension = dimension
        self.limits = limits
        self.function = function
        self.n = n
        self.precision = precision

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

    def SA(self):
        candidate = self.generate_candidate()
        T = 1000

        while T > 0.05:
            for i in range(0, self.n):
                new_candidate = mutation(candidate)
                score = self.evaluate(new_candidate) - self.evaluate(candidate)

                if score < 0:
                    candidate = new_candidate
                elif random.random() < np.exp(-1 * np.abs(score) / T):
                    candidate = new_candidate

            T *= 0.95

        return self.evaluate(candidate)
