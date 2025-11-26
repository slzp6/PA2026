"""c14_9.py"""

import matplotlib.pyplot as plt
import numpy as np

pt_x = np.random.rand(500)
pt_y = np.random.rand(500)
print('x', pt_x[0:10])
print('y', pt_y[0:10])

fig, ax = plt.subplots()
ax.scatter(pt_x, pt_y)
ax.set_title("title")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
# plt.show()
plt.savefig("c14_9.png")
