#Learn how to manipulate large datasets efficiently using NumPy without writing Python loops.
numbers = [1, 2, 3, 4]
result = []

for x in numbers:

    result.append(x * 2) # type: ignore


print(result) # type: ignore

print("\n")
#creating arrays
import numpy as np

a = np.array([1, 2, 3])

print(a)

import numpy as np
a = np.array([1,2, 3, 4, 5, 6, 7])
print(a)
b = np.array([7,7,6,5,4,3,2,2,0])
print(b)
# Multidimentional array
matrix = ([
    [4,6,7],
    [7,9,7]
])
print(matrix)
print(matrix[0][2])

#victorization
#instead of:
numbers = [1,2,3,4,5]
result =[]
for x in numbers:
    result.append(x * 2) # type: ignore
print(result) # type: ignore

#use:
numbers = np.array([1,2,3,4,5])
print(numbers)

numbers = np.array([2,3,5,6,7,8])
print(numbers * 2)

numbers = np.array([2,4,6,8,10])
print(numbers)


# shape (dimention structure of the array)
numbers = np.array([1,2,3,4,5,6,7])
print(numbers.shape)

numbers = np.array([50,70,90,10])
print(numbers.shape)

numbers = np.array([1,3,6,8,5,5])
print(numbers.shape)
# ndim (number of dimensions.)
numbers = np.array([[23,4,5,6,7], [5,7,8,0,0]])
print(numbers.ndim)

numbers = np.array([4,5,6,4,3,2,6])
print(numbers.ndim)

# size  total number of element

numbers = np.array([3,6,66,44,8])
print(numbers.size)

#dtype mean data type
print(numbers.dtype)
numbers = np.array([6.6, 7.6, 4.8, 5.0])
print(numbers.dtype)


numbers = np.array([3,4,6,8,9,3])
print(numbers.shape)
print(numbers.ndim)
print(numbers.size)
print(numbers.dtype)



# index
numbers = np.array([3,4,6,8,9,3])
print(numbers[2])
print(numbers[-2])
print(numbers[0])
print(numbers[5])
print(numbers[-6])

#changing values
numbers[0] = 56

print(numbers)

#slicing

numbers = np.array([1,3,5,6,8,0,6,4,3,2,1,5,77,89])
print(numbers[0:3])
print(numbers[:8])
print(numbers[3:])
print(numbers[6:9])
print(numbers[:0])
print(numbers[0::3])


#creating arrays automatically
zeros = np.zeros(8)
print(zeros)


ones = np.ones(7)
print(ones)

twos = np.full(5, 2)
print(twos)

#np.arrange (make numbers automatic)

numbers = np.arange(0, 10)
print(numbers)

numbers = np.arange(0,20)
print(numbers)

#np.arange(start, stop, step)
numbers = np.arange(0, 10, 3)
print(numbers)


#np.linspace (linspace(start, stop, number_of_values) creates a specific number of evenly spaced values.)
numbers = np.linspace(0, 7, 4)
print(numbers)
numbers = np.linspace(0, 1, 5)
print(numbers)
numbers = np.linspace(0, 100, 6)
print(numbers)


#example


import numpy as np

temp = np.array([1,2,4,6,8,0,8,6,4,3,2,56,78,45,34])
print(temp)
print(numbers.shape)
print(numbers.ndim)
print(numbers.size)
print(numbers.dtype)
print(numbers[0])
print(numbers[0:])
print(numbers[0:4])
print(numbers[2:])
print(numbers[0:10:4])
print(numbers[0:8])

numbers = np.arange(0, 100, 10)
print(numbers)


numbers = np.linspace(0, 100, 5)
print(numbers)
































