"""q14_1.py"""

import matplotlib.pyplot as plt
import seaborn as sns

anscombe = sns.load_dataset('anscombe')
sns.lmplot(x="x",
           y="y",
           col="dataset",
           hue="dataset",
           data=anscombe,
           col_wrap=2,
           ci=95,
           palette="Dark2",
           height=3.0)
# plt.show()
plt.savefig("q14_1.png", dpi=360)
