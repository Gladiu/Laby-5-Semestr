import numpy as np
import math
def func(array, values, step):
    iterations = int(abs(values[1]-values[0])/step)
    solution = []

    minimal = math.inf
    maximal = -math.inf
    for i in range(iterations):
        base = values[0] + i*step
        #value = (value**4)*array[0] + (value**3)*array[1] + (value ** 2) * array[2] + value * array[3] + array[4]
        value  = 0
        for j in range(len(array)):
            value = value + (base ** (len(array)-1-j))*array[j]
        if minimal > value:
            minimal = value
        if maximal < value:
            maximal = value
    return [minimal, maximal]

if __name__=="__main__":

    array = [1, 1, -129, 171, 1620]
    values = [-46, 14]
    step = 1
    print(func(array, values, step))

