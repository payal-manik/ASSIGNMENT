# Use np.where() to replace values 

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
new_arr = np.where(arr > 3, 10, arr)

print("Array after np.where condition:\n", new_arr)