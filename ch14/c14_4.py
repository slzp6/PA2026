"""c14_4.py"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [1, 4, 9, 16, 25]
y3 = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.plot(x, y3, color='red', marker='o', \
         linestyle='dashed',linewidth=3, markersize=12)
ax.plot(x, y2, color='green', marker='o', \
         linestyle='dotted',linewidth=3, markersize=10)
ax.plot(x, y1, color='blue', marker='o', \
         linestyle='dashdot',linewidth=3, markersize=8)
# plt.show()
plt.savefig("c14_4.png")
