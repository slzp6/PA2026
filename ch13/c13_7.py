"""c13_7.py"""

import pandas as pd

fruits = {'name': ["apple", "banana", "cranberry"],\
          'weight': [10, 20, 30], \
          'price': [40, 50, 60]}
idx = ["r0", "r1", "r2"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("---")
print("loc: ", df.loc["r2", "price"])
print("iloc: ", df.iloc[2, 2])
