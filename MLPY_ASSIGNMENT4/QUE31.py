# Concatenate two Series using concat().

import pandas as pd

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

concat_s = pd.concat([s1, s2])

print(concat_s)
