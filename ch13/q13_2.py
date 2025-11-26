"""q13_2.py"""

import pandas as pd

fruits = {"A": [10, 20, 30], \
          "B": [40, 50, 60], \
          "C": [70, 80, 90]}
idx = ["R0", "R1", "R2"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("---")
print("loc: ", df.loc["R1", "B"])
print("iloc: ", df.iloc[1, 1])
