"""q15_1.py"""

# pylint: disable=unbalanced-tuple-unpacking

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))

x, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=42)
ax1.scatter(x[:, 0], x[:, 1], s=3.0)
ax1.set_title("circles")
ax1.set_xticks([])
ax1.set_yticks([])

x, y = make_blobs(n_samples=200, centers=5, cluster_std=1.00, random_state=42)
ax2.scatter(x[:, 0], x[:, 1], s=3.0)
ax2.set_title("blobs")
ax2.set_xticks([])
ax2.set_yticks([])

plt.tight_layout()
# plt.show()
plt.savefig("q15_1.png")
