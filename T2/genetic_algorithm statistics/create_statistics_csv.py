from statistics import mean, stdev
import numpy as np
import pandas as pd


def GA_statistics(function_name, dimension):
    file_path = "../results/"
    file_name = function_name + ".txt"

    df = pd.read_csv(file_path + file_name)
    results = df.loc[df['dimension'] == dimension]

    MEAN = mean(results["value"])
    MIN = results["value"].min()
    MAX = results["value"].max()
    ST_DEV = stdev(results["value"])
    MEAN_TIME = mean(results["time"])

    STATISTICS = [str(MEAN), str(MIN), str(
        MAX), str(ST_DEV), str(MEAN_TIME)]

    return ','.join(STATISTICS)


def main():
    functions_name = ["de_jong", "rastrigin", "schwefel", "michalewicz"]
    dimensions = [5, 10, 30]
    csv_header = "mean,min,max,st_dev,mean_time,function,dimension\n"

    with open("statistics.csv", 'a') as file:
        file.write(csv_header)

        for function_name in functions_name:
            for dimension in dimensions:
                file.write(GA_statistics(function_name, dimension) +
                           ',' + function_name + ',' + str(dimension) + '\n')

    file.close()


main()
