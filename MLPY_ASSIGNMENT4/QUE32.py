# Concatenate two Series using append().

import pandas as pd

s1 = pd.Series([7, 8])
s2 = pd.Series([9, 10])

appended_s = s1.append(s2)

print(appended_s)
