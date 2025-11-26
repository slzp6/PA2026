"""c14_11.py"""

import matplotlib.pyplot as plt
import numpy as np

N = 10000
N_CIRCLE = 0
N_SQUARE = 0

pts_x = []
pts_y = []
pts_stat = []

for _ in range(N):
    x = np.random.uniform(-1, 1)
    pts_x.append(x)

    y = np.random.uniform(-1, 1)
    pts_y.append(y)

for i in range(N):
    dist = pts_x[i]**2.0 + pts_y[i]**2.0

    if dist <= 1.0:
        N_CIRCLE += 1
        pts_stat.append(1)
    else:
        pts_stat.append(0)

    N_SQUARE += 1

pi = 4.0 * N_CIRCLE / N_SQUARE
print(pi)

fig, ax = plt.subplots()
ax.scatter(pts_x, pts_y, c=pts_stat, cmap='summer', s=0.1)
ax.set_aspect('equal')
# plt.show()
plt.savefig("c14_11.png")
