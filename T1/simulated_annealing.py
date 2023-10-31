from optimization_algorithm import *
from utils import swap_bit


def mutate(bitstring):
    mutation_bit = random.randint(0, len(bitstring) - 1)
    return swap_bit(bitstring, mutation_bit)


class SimulatedAnnealing(OptimizationAlgorithm):
    def __init__(self, dimension, limits, function, n=200, precision=3):
        super().__init__(dimension, limits, function, n, precision, mode='')

    def solve(self):
        candidate = self.generate_candidate()
        T = 1000

        while T > 0.05:
            for i in range(0, self.n):
                new_candidate = mutate(candidate)
                score = self.evaluate(new_candidate) - self.evaluate(candidate)

                if score < 0:
                    candidate = new_candidate
                elif random.random() < np.exp(-1 * np.abs(score) / T):
                    candidate = new_candidate

            T *= 0.95

        return self.evaluate(candidate)
