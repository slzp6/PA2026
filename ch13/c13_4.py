"""c13_4.py"""

import pandas as pd

a = [10, 20, 30]

ps = pd.Series(a, index=['a', 'b', 'c'])
print(ps)
