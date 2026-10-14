import numpy as np
matrix = np.array([[10,30,40],[50,60,70],[80,90,20]])
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix[1][0])
print(matrix[1][2])
print(matrix[:2, :2])
matrix = np.arange(1, 13)
print(matrix)
matrix = np.reshape(matrix, (3, 4))
print(matrix)
matrix = matrix.reshape(3, 4)
print(matrix)
print(matrix.T)
print(matrix.flatten())
matrix = np.array([[10,20,30], [40,50,60]])
print(np.sum(matrix, axis=0))
print(np.sum(matrix, axis=1))
# exercise 
import numpy as np

scores = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [95, 88, 92]
])

print("Scores:")
print(scores)

print("\nShape:")
print(scores.shape)

print("\nFirst student:")
print(scores[0])

print("\nMath/Subject 1:")
print(scores[:, 0])

print("\nFirst two students:")
print(scores[:2])

print("\nAverage of each student:")
print(np.mean(scores, axis=1))

print("\nAverage of each subject:")
print(np.mean(scores, axis=0))







































