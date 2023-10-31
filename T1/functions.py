import numpy as np


def de_jongs(parameters):
    np_parameters = np.array(parameters)
    np_parameters = np_parameters ** 2

    return np_parameters.sum()


def michalewicz(parameters):
    np_parameters = np.array(parameters)

    for i in range(0, len(np_parameters)):
        parameter = np_parameters[i]
        np_parameters[i] = np.sin(parameter) * ((np.sin(i * (parameter ** 2) / np.pi)) ** 20)

    return -1 * np_parameters.sum()


def rastrigins(parameters):
    np_parameters = np.array(parameters)
    np_parameters = (np_parameters ** 2) - (10 * np.cos(2 * np.pi * np_parameters))

    return 10 * len(parameters) + np_parameters.sum()


def schwefel(parameters):
    np_parameters = np.array(parameters)
    np_parameters = (-1 * np_parameters) * (np.sin(np.sqrt(np.abs(np_parameters))))

    return np_parameters.sum()
