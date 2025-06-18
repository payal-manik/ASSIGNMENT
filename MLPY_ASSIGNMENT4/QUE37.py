# Drop missing values.

import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, 2, None, 3])
s_dropped = s.dropna()

print(s_dropped)
