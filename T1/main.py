import multiprocessing
from execution import *
from functions import *
import sys


def main():

    algorithm, mode, function, interval, dimension = None, None, None, None, None
    processes_number = 10
    processes = []

    if len(sys.argv) < 5:
        algorithm, mode, function, interval, dimension = get_input_data()
        processes = []
    elif len(sys.argv) == 6:
        algorithm = sys.argv[1]
        mode = sys.argv[2]
        function_number = int(sys.argv[3])
        dimension = int(sys.argv[4])
        processes_number = int(sys.argv[5])

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
    elif len(sys.argv) == 5:
        algorithm = sys.argv[1]
        function_number = int(sys.argv[2])
        dimension = int(sys.argv[3])
        processes_number = int(sys.argv[4])

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

    print(
        f'Starting {algorithm} for {function.__name__} with dimension {dimension}.')

    aux = 1
    for i in range(0, int(30/processes_number)):
        for j in range(0, int(processes_number)):
            p = multiprocessing.Process(target=execute, args=(aux,
                                                              dimension, interval, function, mode, algorithm))
            aux += 1
            processes.append(p)
            p.start()

        for process in processes:
            process.join()


if __name__ == '__main__':
    main()
