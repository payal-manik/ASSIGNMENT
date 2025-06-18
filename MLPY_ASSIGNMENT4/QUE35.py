# Convert Series to DataFrame.

import pandas as pd

s = pd.Series([1, 2, 3], name='Numbers')
df = s.to_frame()

print(df)
