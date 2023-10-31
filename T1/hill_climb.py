from optimization_algorithm import *
from utils import swap_bit


class HillClimbing(OptimizationAlgorithm):
    def __init__(self, dimension, limits, mode, function, n=10000, precision=5):
        super().__init__(dimension, limits, function, n, precision, mode)

    def mutate_first(self, bitstring):
        for i in range(0, len(bitstring)):
            bitstring_copy = bitstring
            bitstring_copy = swap_bit(bitstring_copy, i)

            if self.evaluate(bitstring_copy) < self.evaluate(bitstring):
                return bitstring_copy

        return bitstring

    def mutate_best(self, bitstring):
        best_position = -1
        best_score = self.evaluate(bitstring)

        for i in range(0, len(bitstring)):
            bitstring_copy = bitstring
            bitstring_copy = swap_bit(bitstring_copy, i)

            if self.evaluate(bitstring_copy) < best_score:
                best_position = i
                best_score = self.evaluate(bitstring_copy)

        if best_position == -1:
            return bitstring
        else:
            return swap_bit(bitstring, best_position)

    def mutate_worst(self, bitstring):
        worst_position = -1
        worst_score = self.evaluate(bitstring)

        for i in range(0, len(bitstring)):
            bitstring_copy = swap_bit(bitstring, i)
            score = self.evaluate(bitstring_copy)

            if score < worst_score:
                worst_position = i
                worst_score = score

        if worst_position == -1:
            return bitstring
        else:
            return swap_bit(bitstring, worst_position)

    def mutate(self, bitstring):
        if self.mode == "first":
            return self.mutate_first(bitstring)
        elif self.mode == "best":
            return self.mutate_worst(bitstring)
        elif self.mode == "worst":
            return self.mutate_worst(bitstring)

    def search_minima(self):
        candidate = self.generate_candidate()
        is_local = False

        while not is_local:
            new_candidate = self.mutate(candidate)

            if new_candidate == candidate:
                return self.evaluate(candidate)

            candidate = new_candidate

    def solve(self):
        best = self.search_minima()

        for _ in range(0, self.n):
            minima = self.search_minima()

            if best > minima:
                best = minima

        return best
