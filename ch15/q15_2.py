"""q15_2.py"""

import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.datasets import make_circles

fig, axs = plt.subplots(2, 3, figsize=(9, 6))

cx, cy = make_circles(  # pylint: disable=unbalanced-tuple-unpacking
    n_samples=1_000,
    factor=0.3,
    noise=0.05,
    random_state=42)
axs[0, 0].scatter(cx[:, 0], cx[:, 1], s=3.0)
axs[0, 0].set_title("circles")
axs[0, 0].set_xticks([])
axs[0, 0].set_yticks([])

bx, by = make_blobs(  # pylint: disable=unbalanced-tuple-unpacking
    n_samples=200,
    centers=5,
    cluster_std=1.00,
    random_state=42)
axs[1, 0].scatter(bx[:, 0], bx[:, 1], s=3.0)
axs[1, 0].set_title("blobs")
axs[1, 0].set_xticks([])
axs[1, 0].set_yticks([])

model = KMeans(n_clusters=2, init='k-means++', random_state=42)
model.fit(cx)
print(model.cluster_centers_)
y_pred = model.predict(cx)
axs[0, 1].scatter(cx[:, 0], cx[:, 1], c=y_pred, s=3.0)
axs[0, 1].set_title("KMeans")
axs[0, 1].set_xticks([])
axs[0, 1].set_yticks([])

model = KMeans(n_clusters=5, init='k-means++', random_state=42)
model.fit(bx)
print(model.cluster_centers_)
y_pred = model.predict(bx)
axs[1, 1].scatter(bx[:, 0], bx[:, 1], c=y_pred, s=3.0)
axs[1, 1].set_title("KMeans")
axs[1, 1].set_xticks([])
axs[1, 1].set_yticks([])

db = DBSCAN(eps=0.3, min_samples=2)
db.fit(cx)
labels = db.labels_
axs[0, 2].scatter(cx[:, 0], cx[:, 1], c=labels, s=3.0)
axs[0, 2].set_title("DBSCAN")
axs[0, 2].set_xticks([])
axs[0, 2].set_yticks([])

db = DBSCAN(eps=0.3, min_samples=2)
db.fit(bx)
labels = db.labels_
axs[1, 2].scatter(bx[:, 0], bx[:, 1], c=labels, s=3.0)
axs[1, 2].set_title("DBSCAN")
axs[1, 2].set_xticks([])
axs[1, 2].set_yticks([])

plt.tight_layout()
# plt.show()
plt.savefig("q15_2.png")
