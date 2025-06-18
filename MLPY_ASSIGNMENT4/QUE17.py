# Get the index of the minimum and maximum values

import numpy as np

arr = np.array([3, 1, 7, 2, 9])

min_index = np.argmin(arr)
max_index = np.argmax(arr)

print("Index of min value:", min_index)
print("Index of max value:", max_index)
