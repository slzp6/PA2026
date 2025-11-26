"""c13_14.py"""

import matplotlib.pyplot as plt
import pandas as pd

# FILE_PATH = "./sample_data/california_housing_train.csv"
FILE_PATH = "california_housing_train.csv"

df = pd.read_csv(FILE_PATH)
df.plot(x="longitude", y="latitude", kind="scatter", color="Green")
# plt.show()
plt.savefig("p13_14.png")
