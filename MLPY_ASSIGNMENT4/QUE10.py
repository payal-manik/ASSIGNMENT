#Extract even numbers form an array

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
even_numbers = arr[arr % 2 == 0]

print("Even numbers:", even_numbers)
