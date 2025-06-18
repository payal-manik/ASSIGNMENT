# Sort Series by index.

import pandas as pd

s = pd.Series([100, 200, 300], index=['c', 'a', 'b'])
sorted_s = s.sort_index()

print(sorted_s)
