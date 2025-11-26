"""c13_9.py"""

import pandas as pd

URL = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

iris = pd.read_csv(URL)
print(iris)
