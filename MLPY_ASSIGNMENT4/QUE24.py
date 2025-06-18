# Filter Series elements greater than 50.

import pandas as pd

series = pd.Series([10, 60, 30, 80, 50])
filtered = series[series > 50]

print(filtered)
