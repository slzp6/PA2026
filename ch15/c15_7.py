"""c15_7.py"""

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

x, y = make_blobs(  # pylint: disable=unbalanced-tuple-unpacking
    n_samples=200,
    centers=4,
    cluster_std=1.00,
    random_state=42)

inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(range(1, 11), inertia)
plt.title('K')
plt.xlabel('number of clusters')
plt.ylabel('WCSS')
# plt.show()
plt.savefig("c15_7.png")
