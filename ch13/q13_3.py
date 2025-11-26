"""q13_3.py"""

import pandas as pd

dict_a = {"A": 10, "B": 20, "C": 30}

ps = pd.Series(dict_a)
print(ps)
print("---")
print(ps.sort_values(ascending=False))
