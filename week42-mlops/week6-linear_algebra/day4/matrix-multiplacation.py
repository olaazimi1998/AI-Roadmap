
import numpy as np

A = np.array([[1, 2, 3],
     [4, 5, 6]])

B = np.array([[10, 20],
     [30, 40],
     [50, 60]])

C = A @ B
print(C)

print(np.dot(A, B))


A = np.random.rand(3, 4) # type: ignore
B = np.random.rand(4, 2) # type: ignore

C = A @ B # type: ignore

print(A.shape)
print(B.shape)
print(C.shape)







