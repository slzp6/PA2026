"""c13_6.py"""

import pandas as pd

fruits = {'name': ["apple", "banana", "cranberry"],\
          'weight': [10, 20, 30], \
          'price': [40, 50, 60]}
print(fruits)
print("-----")

df = pd.DataFrame(fruits)
print(df)
