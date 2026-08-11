import numpy as np
a = np.array([10, 20, 30])
b = np.array([50, 60, 70])
#addition
print(a + b)

#or
result = a + b
print(result)

#subtract

print(a - b)

# multiplication
print(a * b)

# @ for multiplication[ in matrix not elements]

#divide
print(a / b)

#power
numbers = np.array([2, 3, 4])
print(numbers ** 2)

#Operations with a Scalar
#You can also operate on the entire array using one numbe
numbers = np.array([3,4,6,7])
#Comparisons 
print(numbers + 3)
print(numbers - 4)
print(numbers > 3)
print(numbers < 5)
print(numbers == 4)


#Boolean Indexing 🔥
#Now we use the Boolean array to filter data.
numbers = np.array([10,20,30,40,50,60,70])
print(numbers[numbers > 30])
print(numbers[numbers < 40])
# np.SUM
print(np.sum(numbers))

#np.mean()
print(np.mean(numbers))
print(np.max(numbers))
print(np.min(numbers))
print(np.std(numbers))
#argmin()
#This returns the index of the smallest valueand big .Numbers))
print(np.argmin(numbers))
print(np.argmax(numbers))


#np.max()      → maximum value # type: ignore
#np.argmax()   → index of maximum # type: ignore


#np.min()       _ minimum value
#np.argmin()    _ index of minimum

#square root
numbers = np.array([2,4,5,7,8,9])
print(np.sqrt(numbers))


#Exponential
print(np.exp(numbers))

#logaritm
print(np.log(numbers))

#rounding
numbers = np.array([2.34, 5.67, 8,98, 5.678, 8,8.6786])
print(np.round(numbers, 1))

#absolute values
numbers = np.array([-17, -34, -4, -6, -45])
print(np.abs(numbers))
#2D Mathematical Operations
#Now let's combine Day 2 with today's lesson

matrix = np.array([[3,4,5], [4, 5,6]])

print(matrix + 10)
print(np.sum(matrix + 70))

print(np.sum(matrix, axis=0))
print(np.sum(matrix, axis=1))

#mean with axis:axis=0 mean of row , axis=1 mean of column
print(np.mean(matrix, axis=0))
print(np.mean(matrix, axis=1))


# Exercise
scores = np.array([
    [20,30,40],
     [30,50,60],
      [70,80,90] 
      ])

print("Total", np.sum(scores))
print("Mean", np.mean(scores))
print("Minimum", np.min(scores))
print("Maximum", np.max(scores))
print("standard devition", np.std(scores))
print()

#mean of column
print(np.mean(scores, axis=0))

#mean of row
print(np.mean(scores, axis=1))

print(scores[scores > 40])
print(scores[scores < 90])

result = scores[(scores >= 50) & (scores <= 70)]
print(result)

result = scores[(scores >= 60) | (scores <= 90)]

print(result)

# & and
# | or




