# A matrix is a rectangular collection of numbers arranged in rows and columns.
import numpy as np
A = np.array([ # type: ignore
    [1, 2],
    [3, 4]
])

A = np.array([ # type: ignore
    [1, 2, 3],
    [4, 5, 6]
])

A = np.array([ # type: ignore
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
#A = (m × n)
#B = (n × p)
#A × B = (m × p)
#
# (2 × 3) × (3 × 4) it will work
#(2 × 3) × (2 × 4) not working


A = np.array([ # type: ignore
    [1, 2],
    [3, 4]
])

B = np.array([ # type: ignore
    [5, 6],
    [7, 8]
])

C = A @ B # C = np.dot(A, B)
print(C)

C = A * B # type: ignore
print(C)

#input → weights → output

x = np.array([2, 3])
w = np.array([0.5, 0.8])

q = x @ w
print(q)


A = np.array([ # type: ignore
    [1, 2, 3],
    [4, 5, 6]
])

print(A.shape)





































