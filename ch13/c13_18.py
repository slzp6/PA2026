"""c13_18.py"""

import pandas as pd

fruits = {"name": [None, "watermelon", "pear"],\
          "weight": [386, 486, None], \
          "price": [None, 9, 19]}
idx = ["r0", "r1", "r2"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("--- A")
print(df.isnull())
print("--- B")
print(df.isnull().sum())
print("--- C")
df_dropna = df.dropna()
print(df_dropna)
print("--- D")
df_fillna = df.fillna(0)
print(df_fillna)
