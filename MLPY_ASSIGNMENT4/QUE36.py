# Replace NaN with 0.

import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, 3])
s_filled = s.fillna(0)

print(s_filled)
