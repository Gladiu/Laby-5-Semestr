import numpy as np
import math
array = [1, 1, -129, 171, 1620]
values = [-46, 14]
step = 1
iterations = int(abs(values[1]-values[0])/step)
solution = []

minimal = math.inf
maximal = -math.inf
for i in range(iterations):
    value = values[0] + i*step
    value = (value**4)*array[0] + (value**3)*array[1] + (value ** 2) * array[2] + value * array[3] + array[4]
    if minimal > value:
        minimal = value
    if maximal < value:
        maximal = value

print(minimal)
print(maximal)
