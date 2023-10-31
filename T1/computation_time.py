import timeit
import matplotlib.pyplot as plt

from hill_climb import HillClimbing
from execution_parameters import *

# Define the optimization parameters
start_dimension = 1
end_dimension = 30
iterations = 5
precision = 5

# Initialize lists to store dimensions and corresponding execution times
dimensions = []
execution_times = []


# Function to perform the optimization and measure execution time
def optimize_dimension(test_dimension):
    HC = HillClimbing(test_dimension, interval, mode, function, n=iterations, precision=precision)
    return timeit.timeit(HC.solve, number=1)


# Loop through dimensions and optimize
for dimension in range(start_dimension, end_dimension + 1):
    execution_time = optimize_dimension(dimension)
    dimensions.append(dimension)
    execution_times.append(execution_time)


# Function to plot the results
def plot_results(test_dimensions, test_execution_times):
    plt.xlabel("Dimension")
    plt.ylabel("Time (s)")
    plt.plot(test_dimensions, test_execution_times)
    plt.show()


# Run
if __name__ == '__main__':
    plot_results(dimensions, execution_times)
