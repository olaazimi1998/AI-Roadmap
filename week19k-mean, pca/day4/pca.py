import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# Customer data
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


# Scale the data
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# Create PCA
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)


# Print result
print("Original shape:")
print(X.shape)

print("\nPCA shape:")
print(X_pca.shape)

print("\nPCA data:")
print(X_pca)


# Visualize
plt.scatter(
    X_pca[1:, 0],
    X_pca[1:, 1]
)

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")

plt.title("PCA Visualization")

plt.show()