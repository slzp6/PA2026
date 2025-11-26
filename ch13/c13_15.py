"""c13_15.py"""

import matplotlib.pyplot as plt
import pandas as pd

# FILE_PATH = "./sample_data/california_housing_train.csv"
FILE_PATH = "california_housing_train.csv"

df = pd.read_csv(FILE_PATH)
df.plot(x="median_income",
        y="median_house_value",
        kind="scatter",
        color="Blue")
# plt.show()
plt.savefig("p13_15.png")
