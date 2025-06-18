# Reshape 1D array to 2D

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])
arr_2d = arr_1d.reshape(2, 3)

print("2D array:\n", arr_2d)
