# Check for null values.

import pandas as pd
import numpy as np

s = pd.Series([1, np.nan, 3, None])
null_check = s.isnull()

print(null_check)
