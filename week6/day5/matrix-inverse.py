#matrix inverse:
# 1. What is a Matrix Inverse?
#
#Suppose we have:
#
# A = \begin{bmatrix} 2 & 1\\ 1 & 1 \end{bmatrix} $$
#
#The inverse of A is written as:
#
# A^{-1} 
#
#The important property is:
#
# A A^{-1} = I 
#
#where I is the identity matrix.

import numpy as np
A = np.array([
    [2, 1],
    [1, 1]
])

b = np.array([[5, 3],
     [1,3]])

A_inverse = np.linalg.inv(A)

x = A_inverse @ b

print(x)


























