"""c13_19.py"""

import pandas as pd

fruits = {"name": [None, "watermelon", "pear", "pear"],\
          "weight": [386, 486, None, None], \
          "price": [None, 9, 19, 19]}
idx = ["r0", "r1", "r2", "r3"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("--- A")
df_duplicated = df.duplicated()

print("--- B")
df_drop_duplicated = df.drop_duplicates()
print(df_drop_duplicated)
