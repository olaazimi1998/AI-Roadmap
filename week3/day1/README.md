import numpy as np

# Create
a = np.array([1, 2, 3])

# Information
a.shape
a.ndim
a.size
a.dtype

# Indexing
a[0]
a[-1]

# Slicing
a[:2]
a[1:]
a[::2]
a[::-1]

# Modify
a[0] = 100

# Create special arrays
np.zeros(5)
np.ones(5)
np.arange(0, 10, 2)
np.linspace(0, 1, 5)