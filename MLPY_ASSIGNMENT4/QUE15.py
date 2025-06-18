# Find the unique values and their counts

import numpy as np

arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])

unique_values, counts = np.unique(arr, return_counts=True)
print("Unique values:", unique_values)
print("Counts:", counts)
