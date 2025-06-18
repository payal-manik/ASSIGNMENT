# Create a Series from a dictionary.

import pandas as pd

data = {'x': 1, 'y': 2, 'z': 3}
series = pd.Series(data)

print(series)
