"""c14_6.py"""

import matplotlib.pyplot as plt

x = ["10", "20", "30", "40", "50", "60", "70"]
y = [2847, 13953, 11994, 14685, 16510, 11504, 9448]

fig, ax = plt.subplots()
ax.bar(x=x, height=y, color='green', edgecolor='blue', \
         linewidth=1)
ax.set_title("undergraduate students (2024)")
ax.set_xlabel("age intervals")
ax.set_ylabel("N")
# plt.show()
plt.savefig("c14_6.png")
