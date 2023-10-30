from hill_climb import HillClimbing
from simulated_annealing import SimulatedAnnealing
from functions import *
import time

# In case the user did not specified as parameters to executable
# Read the info in real time from him
def get_input_data():
    algorithm = input("Enter algorithm(HC or SA): ")

    if algorithm != "HC" and algorithm != "SA":
        print("Error..enter a known algorithm")
        exit(0)

    mode = None

    if algorithm == "HC":
        mode = input("Enter mode(first | best | worst): ")

        if mode != "first" and mode != "best" and mode != "worst":
            print("Error..enter a known mode")
            exit(0)

    function = None
    function_number = int(input(
        "1 --- De Jong's\n2 --- Schwefel\n3 --- Rastring's\n4 --- Michalewicz\nEnter function number: "))
    interval = []

    if function_number == 1:
        function = de_jongs
        interval = [-5.12, 5.12]
    elif function_number == 2:
        function = schwefel
        interval = [-500, 500]
    elif function_number == 3:
        function = rastrigins
        interval = [-5.12, 5.12]
    elif function_number == 4:
        function = michalewicz
        interval = [0, np.pi]
    else:
        print("Error..enter a known function")

    dimension = int(input("Enter dimension: "))

    return algorithm, mode, function, interval, dimension


def write_to_file(file_name, content):
    f = open(file_name, 'a')
    f.write(str(content))
    f.write("\n")
    f.close()

# execute the algorithms 
def execute(thread_number, dimension, interval, function, mode=None, algorithm="HC"):
    results_file_name = f'{algorithm}_{dimension}_{function.__name__}'
    directory_name = 'results'

    if mode is not None:
        results_file_name = mode + results_file_name

    if algorithm == "HC" and mode is None:
        print("Enter mode")
        exit(0)
    elif algorithm == "HC" and mode is not None:
        HC = HillClimbing(dimension, interval, mode,function, n=200, precision=4)

        start_time = time.time()
        minima = HC.HC()
        print(minima)

        # format saved "thread number | value | delta time"
        write_to_file(directory_name + '/' + results_file_name,f'{thread_number}. {format(minima, ".4f")} ---- {format(time.time() - start_time, ".2f")}')
    elif algorithm == "SA":
        SA = SimulatedAnnealing(dimension, interval,function, n=1000, precision=4)

        start_time = time.time()
        minima = SA.SA()
        print(minima)

        # format saved "thread number | value | delta time"
        write_to_file(directory_name + '/' + results_file_name, f'{thread_number}. {format(minima, ".4f")} ---- {format(time.time() - start_time, ".2f")}')
