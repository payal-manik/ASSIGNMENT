# Stack two arrays vertically

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vertical_stack = np.vstack((a, b))
print("Vertical stack:\n", vertical_stack)
