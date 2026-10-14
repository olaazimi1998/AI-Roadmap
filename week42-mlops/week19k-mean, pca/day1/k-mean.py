#K-Means is one of the most popular clustering algorithms.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Customer data
# Column 1 = Age
# Column 2 = Income

X = np.array([
    [20, 2000],
    [22, 2200],
    [25, 2500],
    [30, 3000],

    [40, 5000],
    [42, 5200],
    [45, 5500],
    [48, 5800],

    [55, 8000],
    [58, 8500],
    [60, 9000],
    [62, 9500]
])


# Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42
)


# Train the model
model.fit(X)


# Get cluster labels
labels = model.labels_

print("Cluster labels:")
print(labels)


# Get cluster centers
print("\nCluster centers:")
print(model.cluster_centers_)


# Visualize clusters
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels
)

plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Customer Segmentation with K-Means")

plt.show()
#Income
 # |
 # |                  ● ● ●
 # |                ● ● ●
 # |
 # |
 # |       ● ● ●
 # |      ● ●
 # |
 # |                         ● ●
 # |                        ● ●
 # +------------------------------ Age # type: ignore




 