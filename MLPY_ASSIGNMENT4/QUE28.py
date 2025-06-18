# Sort Series by values descending.

import pandas as pd

s = pd.Series([10, 50, 30, 20])
sorted_s = s.sort_values(ascending=False)

print(sorted_s)
