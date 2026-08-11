import numpy as np

# 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Information
matrix.shape
matrix.ndim
matrix.size

# Element
matrix[0, 1]

# Row
matrix[0]

# Column
matrix[:, 0]

# Slicing
matrix[:2, :2]

# Reshape
matrix.reshape(3, 2)

# Flatten
matrix.flatten()

# Transpose
matrix.T

# Axis
np.sum(matrix, axis=0)
np.sum(matrix, axis=1)