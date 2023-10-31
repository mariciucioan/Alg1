from statistics import mean, stdev


def get_line_content(line):
    split_line = line.split(" ")
    value = float(split_line[1])
    execution_time = float(split_line[-1])

    return [value, execution_time]


def get_file_content(path):
    f = open(path, 'r')
    data = []

    for _ in range(0, 30):
        line = f.readline()
        data.append(get_line_content(line))

    return data


def statistics(path):
    data = get_file_content(path)
    results = []
    time = []

    for d in data:
        results.append(d[0])
        time.append(d[1])

    mean_results = mean(results)
    std = stdev(results)
    mean_execution_time = mean(time)

    return mean_results, std, mean_execution_time


if __name__ == '__main__':
    path = 'results/HC_best_5_de_jongs'

    f = open('results/statistics.csv', 'a')
    f.write(str(statistics(path)))
    f.write('\n')
    f.close()
