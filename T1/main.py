import multiprocessing
from execution import *
from functions import *


def main():

    algorithm, mode, function, interval, dimension = None, None, None, None, None
    processes_number = 10
    processes = []

    algorithm, mode, function, interval, dimension = get_input_data()
    processes = []
    
    print(f'Starting {algorithm}. Function: {function.__name__}. Dimension: {dimension}.')

    aux = 1
    for i in range(0, int(30/processes_number)):
        for j in range(0, int(processes_number)):
            p = multiprocessing.Process(target=execute, args=(aux,dimension, interval, function, mode, algorithm))
            aux += 1
            processes.append(p)
            p.start()

        for process in processes:
            process.join()


if __name__ == '__main__':
    main()
