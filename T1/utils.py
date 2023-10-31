import math
from functions import *


def write_to_file(file_name, content):
    f = open(file_name, 'a')
    f.write(str(content))
    f.write("\n")
    f.close()


def get_interval_for_function(function):
    if function == de_jongs or function == rastrigins:
        return [-5.12, 5.12]
    elif function == schwefel:
        return [-500, 500]
    elif function == michalewicz:
        return [0, math.pi]


def swap_bit(bitstring, bit_pos):
    result = ''
    for i in range(0, len(bitstring)):
        if i == bit_pos:
            result += str(-1 * (int(bitstring[i]) - 1))
        else:
            result += bitstring[i]
    return result
