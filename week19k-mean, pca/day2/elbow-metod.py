import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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

inertia_values = []

for k in range(1, 11):
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)
    inertia_values.append(model.inertia_)


print("Inertia values:")

for k, inertia in zip(range(1, 11), inertia_values):
    print(f"K = {k}, Inertia = {inertia}")


# Plot Elbow Curve
plt.plot(
    range(1, 11),
    inertia_values,
    marker="o"
)

plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")

plt.show()




