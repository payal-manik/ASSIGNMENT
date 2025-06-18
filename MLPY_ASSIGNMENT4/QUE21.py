# Create a Series with custom string indices.

import pandas as pd

data = [100, 200, 300]
indices = ['a', 'b', 'c']
series = pd.Series(data, index=indices)

print(series)
