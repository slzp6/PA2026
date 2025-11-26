"""c13_3.py"""

import pandas as pd

a = [10, 20, 30]

ps = pd.Series(a)
print(ps)
print("---")
print(ps[0], ps[1], ps[2])
