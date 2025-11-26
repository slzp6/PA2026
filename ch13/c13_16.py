"""c13_16.py"""

import pandas as pd

fruits = {"name": ["orange", "watermelon", "pear"],\
          "weight": [386, 486, 286], \
          "price": [12, 9, 19]}
idx = ["r0", "r1", "r2"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("---")
df_name = df.sort_values(by='name')
print(df_name)
print("---")
df_weight = df.sort_values(by='weight')
print(df_weight)
