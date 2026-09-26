#English
#PyTorch is a Python framework for building and training neural networks.

#You already built a neural network using NumPy in Week 25
#.

#Now we're going to build the same kind of neural network using PyTorch.



import numpy as np

x = np.array([1, 2, 3])

import torch

x = torch.tensor([1, 2, 3])
print(x)

print(x.shape)
print(x[1])

x = torch.tensor([
    [1, 2, 3],
    [4, 5, 6]
])

print(x)
print(x.shape)

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print(a + b)
print(a % b)

print(a + b)
print(a - b)
print(a * b)

a = torch.tensor([
    [2, 2],
    [2, 4]
])

b = torch.tensor([
    [4, 5],
    [6, 8]
])


x = torch.zeros(2, 3)
print(x)


x = torch.ones(2, 3)
print(x)

x = torch.rand(2, 3)
print(x)


print(torch.matmul(a, b))
result = a @ b

print(result)
#device = "cuda" if torch.cuda.is_available() else "cpu"

#print(device)