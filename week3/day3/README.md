import numpy as np

# Element-wise
a + b
a - b
a * b
a / b
a ** 2

# Scalar
a + 10
a * 2

# Statistics
np.sum(a)
np.mean(a)
np.min(a)
np.max(a)
np.std(a)

# Index of min/max
np.argmin(a)
np.argmax(a)

# Math functions
np.sqrt(a)
np.exp(a)
np.log(a)
np.abs(a)
np.round(a, 2)

# Comparisons
a > 10
a < 10
a == 10
a >= 10
a <= 10

# Filtering
a[a > 10]

# Multiple conditions
a[(a > 10) & (a < 50)]
a[(a < 10) | (a > 50)]

# Axis
np.sum(matrix, axis=0)
np.sum(matrix, axis=1)

np.mean(matrix, axis=0)
np.mean(matrix, axis=1)