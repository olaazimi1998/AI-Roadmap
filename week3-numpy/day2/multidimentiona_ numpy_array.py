import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70])
print(a)
print(a.shape)
print(a.ndim)


a =np.array([
    [10, 20, 30, 40], 
    [20, 40, 60, 80]])
print(a.shape)
print(a.ndim)



# matrix.shape = (rows, columns) (4, 5)

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix[1, 1])
print(matrix[2, 2])

#        column
#         0   1   2
#       ┌────────────
#row 0  │ 10  20  30
#row 1  │ 40  50  60
#row 2  │ 70  80  90

# matrix[row, column]

print(matrix[0])

#Get an Entire Column

print(matrix[:, 2])

# 2D Slicingmatrix = np.array([
matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

#take first two row
print(matrix[:2])

#take first two row and two column
print(matrix[:2, :2])
# matrix[row_start:row_stop, column_start:column_stop]

print(matrix[1:, 1:])


# reshape()  change the array
numbers = np.arange(1, 13)
print(numbers.shape)
matrix = numbers.reshape(6,2)
print(matrix)


numbers = np.arange(12)
matrix = numbers.reshape(3, 4)
print(matrix)

# flatten()if you want to convert a 2D array back into 1D
#the elements must be the same

#    2D
#     ↓
#    flatten()
#     ↓
#    1D
#
matrix = np.array([[4,5,6,7], [6,7,8,9]])
print(matrix.flatten())

matrix = np.array([[5,5,6],
             [5,4,3]])
print(matrix.flatten())


# transpise the row and column change its position

matrix = np.array([[2,4,6], [2,5,6], [5,6,7]])
print(matrix.T)
print(matrix)


#axis
matrix = np.array([[2,3,4], [6,7,8]])
print(matrix.shape)

#axis=0  operation up to down the row   
#axis=1 operation left to right across the column

print(np.sum(matrix))
print(np.sum(matrix, axis=0))
print(np.sum(matrix, axis=1))
print(matrix[:, 0])

#3D array
data = np.array([
    [
        [1,2,3],
        [3,4,5]
    ],
    [
        [2,3,4],
        [4,6,7]
        ]
        ])
print(data)
#output(2,2,3)
#this is 3D array it has 2 block, 2 row, and 3 column


print(data[0, 0, 1])
#data[block, row, column]







