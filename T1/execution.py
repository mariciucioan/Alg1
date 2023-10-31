import time

from hill_climb import HillClimbing
from simulated_annealing import SimulatedAnnealing
from utils import write_to_file


def execute_algorithm(algorithm, mode, function, dimension, thread_number, interval):
    results_file_name = f'{algorithm}{"_" + mode if algorithm == "HC" else ""}_{dimension}_{function.__name__}'
    results_file = 'results/' + results_file_name

    minima = 0
    start_time = time.perf_counter()

    if algorithm == "HC" and mode is not None:
        minima = HillClimbing(dimension, interval, mode, function, n=200, precision=5).solve()
    elif algorithm == "SA":
        minima = SimulatedAnnealing(dimension, interval, function, n=1000, precision=5).solve()

    write_to_file(results_file, f'{thread_number}. {minima:.4f} ---- {time.perf_counter() - start_time:.2f}')
