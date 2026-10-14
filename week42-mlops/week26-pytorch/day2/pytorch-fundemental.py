#Day 2 — Autograd & Computational Graph
#1. What is Autograd?
#English
#Autograd is PyTorch's automatic differentiation system.
#
#It calculates derivatives/gradients for us.
#
#For example:
#
import torch
x = torch.tensor(3.0, requires_grad=True)

y = x ** 2
y.backward()

print("x:", x)
print("y:", y)
print("gradient:", x.grad)


import torch

x = torch.tensor(2.0, requires_grad=True)

w = torch.tensor(4.0, requires_grad=True)

b = torch.tensor(1.0, requires_grad=True)

y = w * x + b

loss = y ** 2

loss.backward()

print("y:", y)
print("loss:", loss)

print("dx:", x.grad)
print("dw:", w.grad)
print("db:", b.grad)


import torch
import torch.nn as nn 
class MyModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.linear = nn.Linear(1,1)

    def forward(self, x):
        return self.linear(x)


model = MyModel()

print(model)

