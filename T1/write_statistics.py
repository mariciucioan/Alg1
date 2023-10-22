from execution_statistics import statistics


f = open("statistics.csv", 'a')
f.write("function, dimension, algorithm, mean, std, MET\n")

functions_name = ['de_jongs', 'rastrigins', 'michalewicz', 'schwefel']
function_dimensions = ['5', '10', '30']


# Hill Climb best
for function in functions_name:
    for dimension in function_dimensions:
        file_name = f'results/bestHC_{dimension}_{function}.txt'
        mean_results, std, mean_execution_time = statistics(file_name)
        line = [function, dimension, "HC best", str(
            mean_results), str(std), str(mean_execution_time), '\n']
        f.write(','.join(line))


# Hill Climb first
for function in functions_name:
    for dimension in function_dimensions:
        file_name = f'results/firstHC_{dimension}_{function}.txt'
        mean_results, std, mean_execution_time = statistics(file_name)
        line = [function, dimension, "HC first", str(
            mean_results), str(std), str(mean_execution_time), '\n']
        f.write(','.join(line))


# Simulated Annealing
for function in functions_name:
    for dimension in function_dimensions:
        file_name = f'results/SA_{dimension}_{function}.txt'
        mean_results, std, mean_execution_time = statistics(file_name)
        line = [function, dimension, "SA", str(
            mean_results), str(std), str(mean_execution_time), '\n']
        f.write(','.join(line))
