# Stack two arrays horizontally

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

horizontal_stack = np.hstack((a, b))
print("Horizontal stack:", horizontal_stack)
