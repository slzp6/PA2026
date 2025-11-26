"""c13_13.py"""

import pandas as pd

# FILE_PATH = "./sample_data/california_housing_train.csv"
FILE_PATH = "california_housing_train.csv"

df = pd.read_csv(FILE_PATH)
print("--- head(3) ")
print(df.head(3))
print("--- tail(3)")
print(df.tail(3))
print("--- describe (median_house_value)")
print(df["median_house_value"].describe())
