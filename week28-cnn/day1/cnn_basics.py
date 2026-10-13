#CNN = Convolutional Neural Network

import torch

image = torch.tensor([
    [1., 2., 3.],
    [4., 5., 6.],
    [7., 8., 9.]
])

print(image)
print(image.shape)

kernel = torch.tensor([
    [1., 0.],
    [0., 1.]
])



import torch
import torch.nn as nn

conv = nn.Conv2d(
    in_channels=1,
    out_channels=2,

    kernel_size=3
)

print(conv)

image = torch.randn(1, 1, 28, 28)

output = conv(image)
print("Input:", image.shape)
print("Output:", output.shape)

