"""c13_8.py"""

import pandas as pd

fruits = {'name': ["apple", "banana", "cranberry"],\
          'weight': [10, 20, 30], \
          'price': [40, 50, 60]}
idx = ["r0", "r1", "r2"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("\n--- loc")
print(df.loc["r0":"r1", ["name", "weight"]])
print("\n--- iloc")
print(df.iloc[0:1, [0, 1]])
