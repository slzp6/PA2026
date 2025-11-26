"""c13_17.py"""

import pandas as pd

fruits = {"name": ["orange", "watermelon", "pear"],\
          "weight": [386, 486, 286], \
          "price": [12, 9, 19]}
idx = ["r0", "r1", "r2"]

df = pd.DataFrame(fruits, index=idx)
print(df)
print("---")
df_name = df.sort_values(by="name", \
    ascending=False, ignore_index=True )
print(df_name)
