import torch.nn as nn
from torchvision import models


class ResNetClassifier(nn.Module):

    def __init__(self, num_classes=10):
        super().__init__()

        self.model = models.resnet18(
            weights=models.ResNet18_Weights.DEFAULT
        )

        # Fashion-MNIST has 1 channel, so replace the first convolution
        self.model.conv1 = nn.Conv2d(
            1,
            64,
            kernel_size=7,
            stride=2,
            padding=3,
            bias=False,
        )

        # Freeze the pretrained backbone and keep only the final classifier trainable.
        for param in self.model.parameters():
            param.requires_grad = False

        self.model.fc = nn.Linear(
            self.model.fc.in_features,
            num_classes,
        )
        self.model.fc.weight.requires_grad = True
        self.model.fc.bias.requires_grad = True

    def forward(self, x):
        return self.model(x)

    