import numpy as np
# 2.1
print(pow(3, 12)-5)

print(np.array([[2, 0.5]]) @ np.array([[1, 4], [-1, 3]]) @ np.array([[-1], [-3]]))

print(np.linalg.matrix_rank(np.array([[1, -2, 0], [-2, 4, 0], [2, -1, 7]])))

print(np.linalg.inv(np.array([[1, 2], [-1, 0]])) @ np.array([[-1], [2]]))

# 2.2 
array = [1, 1, -129, 171, 1620]
values = [-46, 14]

for i in range(2):
    value = 0
    for j in range(5):
        value = value + pow(values[i], j) * array[4 - j]
    print(value)
