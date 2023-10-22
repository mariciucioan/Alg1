from hill_climb import HillClimbing
from functions import *
import timeit
import matplotlib.pyplot as plt

# Define the optimization parameters
start_dimension = 1
end_dimension = 20
iterations = 3
precision = 3
search_range = [-500, 500]

# Initialize lists to store dimensions and corresponding execution times
dimensions = []
execution_times = []


# Function to perform the optimization and measure execution time
def optimize_dimension(dimensions):
    HC = HillClimbing(dimensions, search_range, "best", schwefel, n=iterations, precision=precision)
    execution_time = timeit.timeit(HC.HC, number=1)  # Measure execution time
    return execution_time


# Loop through dimensions and optimize
for dimension in range(start_dimension, end_dimension + 1):
    execution_time = optimize_dimension(dimension)
    dimensions.append(dimension)
    execution_times.append(execution_time)


# Function to plot the results
def plot_results(dimensions, execution_times):
    plt.xlabel("Dimension")
    plt.ylabel("Time (s)")
    plt.plot(dimensions, execution_times)
    plt.show()


# Plot the results
plot_results(dimensions, execution_times)
