#English:
#Today you will learn:
#
#What matrix multiplication means
#
#Difference between * and @
#
#np.dot()
#
#Matrix shapes
#
#Rules for matrix multiplication
#
#Practical Machine Learning example
#
#Exercises


import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

print(A)

print(A.shape)


a = np.array([
    [1,2],
    [3,4]])

b = ([[4,5],
      [6,7]])

print(a * b)

print(a @ b)


c = np.dot(a, b)
print(c)

#A = (m, n)
#B = (n, p)

#(m, p)
#in this case we cant write this
# A = (2, 3)
#
# B = (2, 4)
# we cant write (2,3)  3!=2  (2, 4)



import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

print(A.shape)
print(B.shape)

C = A @ B

print(C)
print(C.shape)


import numpy as np

A = np.random.rand(1000, 500)
B = np.random.rand(500, 300)

C = A @ B

print(A.shape)
print(B.shape)
print(C.shape)


import numpy as np

A = np.array([[2,3,4],
      [3,4,5]])

B = np.array([[7,5,7],
      [9,5,6]])
V = B.T
print(A @ B.T)
print(np.dot(A , V))





























