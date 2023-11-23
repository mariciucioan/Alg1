import multiprocessing

from execution_parameters import *
from execution import execute_algorithm

if __name__ == '__main__':
    processes = []
    thread_number = 1

    for i in range(0, int(30 / processes_number)):
        for j in range(0, int(processes_number)):
            p = multiprocessing.Process(target=execute_algorithm, args=(algorithm, mode, function, dimension,
                                                                                thread_number, interval))
            thread_number += 1
            processes.append(p)
            p.start()

        for process in processes:
            process.join()
