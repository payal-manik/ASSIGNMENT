# Access first 3 elements of a Series.

import pandas as pd

series = pd.Series([5, 10, 15, 20, 25])
first_three = series.head(3)

print(first_three)
