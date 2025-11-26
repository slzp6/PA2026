"""c14_7.py"""

import matplotlib.pyplot as plt
import numpy as np

labels = ["10", "20", "30", "40", "50", "60", "70"]
y_pos = np.arange(len(labels))
values = [2847, 13953, 11994, 14685, 16510, 11504, 9448]
fig, ax = plt.subplots()
ax.barh(y=y_pos, width=values, \
        color='green', edgecolor='blue', linewidth=1)
ax.set_title("undergraduate students (2024)")
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.set_xlabel("N")
ax.set_ylabel("age intervals")
# plt.show()
plt.savefig("c14_7.png")
