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


class HillClimbing:
    def __init__(self, dimension, limits, mode, function, n=10000, precision=3):
        self.dimension = dimension
        self.limits = limits
        self.mode = mode
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

    def mutation(self, bitstring):
        initial_score = self.evaluate(bitstring)
        bitstring_length = len(bitstring)

        if self.mode == 'first':
            for i in range(0, bitstring_length):
                bitstring_copy = bitstring
                bitstring_copy = swap_bit(bitstring_copy, i)

                if self.evaluate(bitstring_copy) < initial_score:
                    return bitstring_copy

            return bitstring

        elif self.mode == 'best':
            best_position = -1
            best_score = initial_score

            for i in range(0, bitstring_length):
                bitstring_copy = bitstring
                bitstring_copy = swap_bit(bitstring_copy, i)

                if self.evaluate(bitstring_copy) < best_score:
                    best_position = i
                    best_score = self.evaluate(bitstring_copy)

            if best_position == -1:
                return bitstring
            else:
                return swap_bit(bitstring, best_position)
            
        elif self.mode == 'worst':
            worst_position = -1
            worst_score = initial_score

            for i in range(0, bitstring_length):
                bitstring_copy = swap_bit(bitstring, i)
                score = self.evaluate(bitstring_copy)

                if score < worst_score:
                    worst_position = i
                    worst_score = score

            if worst_position == -1:
                return bitstring
            else:
                return swap_bit(bitstring, worst_position)

    def search_minima(self):
        candidate = self.generate_candidate()
        is_local = False

        while not is_local:
            new_candidate = self.mutation(candidate)

            if new_candidate == candidate:
                return self.evaluate(candidate)

            candidate = new_candidate

    def HC(self):
        best = self.search_minima()

        for _ in range(0, self.n):
            minima = self.search_minima()
            # print("Minima is " + str(minima))

            if best > minima:
                best = minima

        return best
