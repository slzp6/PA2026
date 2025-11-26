"""q14_2.py"""

import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species")
# plt.show()
plt.savefig("q14_2.png")
