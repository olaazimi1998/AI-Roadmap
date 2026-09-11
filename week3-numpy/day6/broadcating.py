import numpy as np

A = np.array([
    [2, 4, 6],
    [1, 3, 5]
])

B = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print(A.shape)
print(B.shape)
result = A @ B
print(result)
# Find:
# 1. A.shape
# 2. B.shape
# 3. A @ B
# 4. Result shape
#
#Broadcasting is a NumPy mechanism that allows
#operations between arrays with different shapes,
#when those shapes are compatible

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([10, 20, 30])

print(A + B)

# output[[11 22 33]
       # [14 25 36]] 
# if you see a broadcasting:
# see the shapes fron right to left:
#for example
#(4, 3) (3,) its comptaible
#(2, 3) (2, 4) its not

A = np.ones((2, 3))
B = np.ones((2, 3))

print(A + B)

#subtract
A = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

B = np.array([10, 20, 30])

print(A - B)

#multiplacation
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([10, 20, 30])

print(A * B)

data = np.array([[10,20,30],
                  [40,50,60],
                  [70,80,90]])
mean = np.array([10,20,30])

normalized = data - mean

print(normalized)

#vectorization
#perform operations on arrays without manually looping through elements

#Broadcasting
#Make compatible arrays with different shapes work together.

A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

B = np.array([
    [1],[2],[3]
])

result = A + B

print(result)
print(A.shape)
print(B.shape)


