"""c15_3.py"""

import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
# print(iris['DESCR'])
data = iris['data']
target = iris['target']

feature_names = iris['feature_names']
df = pd.DataFrame(data=data, columns=feature_names)
print(df.head())
