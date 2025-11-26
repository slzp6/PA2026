"""c13_10.py"""

import datetime

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": ["one", "two", "three"] * 2,
    "B": ["x", "y", "z"] * 2,
    "D": np.random.randn(6),
    "E": np.random.randn(6),
    "F": [datetime.datetime(2024, i, 1) for i in range(1, 7)]
})
print(df)
