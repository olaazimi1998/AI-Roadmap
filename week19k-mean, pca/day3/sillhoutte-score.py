import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


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


# Store results
inertia_values = []
silhouette_values = []

k_values = range(2, 11)


# Test different K values
for k in k_values:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X)

    # Inertia
    inertia_values.append(model.inertia_)

    # Silhouette Score
    score = silhouette_score(X, labels)

    silhouette_values.append(score)


# Print results
print("K Comparison")
print("-" * 30)

for k, inertia, score in zip(
    k_values,
    inertia_values,
    silhouette_values
):
    print(
        f"K = {k} | "
        f"Inertia = {inertia:.2f} | "
        f"Silhouette = {score:.3f}"
    )


# -------------------------
# Elbow Plot
# -------------------------

plt.figure()

plt.plot(
    k_values,
    inertia_values,
    marker="o"
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()


# -------------------------
# Silhouette Plot
# -------------------------

plt.figure()

plt.plot(
    k_values,
    silhouette_values,
    marker="o"
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette Score")

plt.show()