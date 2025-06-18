# Replace NaN with column means

import numpy as np

arr = np.array([[1, 2, np.nan],
                [4, np.nan, 6],
                [7, 8, 9]], dtype=float)

col_means = np.nanmean(arr, axis=0)
inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_means, inds[1])

print("Array after replacing NaNs with column means:\n", arr)
