# Find the max in each row

import numpy as np

arr = np.array([[1, 5, 2],
                [9, 3, 7],
                [4, 8, 6]])

max_in_rows = np.max(arr, axis=1)
print("Max in each row:", max_in_rows)
