import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# -------------------------
# Customer data
# -------------------------

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


# -------------------------
# Step 1: Scale
# -------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# -------------------------
# Step 2: K-Means
# -------------------------

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

labels = model.fit_predict(X_scaled)


# -------------------------
# Step 3: PCA
# -------------------------

pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)


# -------------------------
# Step 4: Print results
# -------------------------

print("Cluster labels:")

print(labels)


print("\nPCA shape:")

print(X_pca.shape)


# -------------------------
# Step 5: Visualization
# -------------------------

plt.scatter(
    X_pca[:, 0],
    X_pca[:, 1],
    c=labels
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.title("Customer Segmentation with K-Means + PCA")

plt.show()