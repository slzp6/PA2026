"""c15_6.py"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

x, y = make_blobs(  # pylint: disable=unbalanced-tuple-unpacking
    n_samples=200,
    centers=4,
    cluster_std=1.00,
    random_state=42)
plt.scatter(x[:, 0], x[:, 1])
# plt.show()
plt.savefig("c15_6a.png")

model = KMeans(n_clusters=4, init='k-means++', random_state=42)
model.fit(x)
print(model.cluster_centers_)
print(model.labels_)
y_pred = model.predict(x)
plt.scatter(x[:, 0], x[:, 1], c=y_pred)

# plt.show()
plt.savefig("c15_6b.png")
