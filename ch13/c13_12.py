"""c13_12.py"""

import pandas as pd

df = pd.read_csv('./fruits.csv', index_col=0)
print(df)
print("\n--- head(2)")
print(df.head(2))
print("\n--- tail(2)")
print(df.tail(2))
print("\n--- describe (price)")
print(df["price"].describe())
