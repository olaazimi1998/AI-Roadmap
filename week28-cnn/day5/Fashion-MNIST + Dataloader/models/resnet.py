import torch.nn as nn

from torchvision import models


class ResNetClassifier(nn.Module):

    def __init__(self, num_classes=10):

        super().__init__()

        self.model = models.resnet18(
            weights=models.ResNet18_Weights.DEFAULT
        )

        self.model.conv1 = nn.Conv2d(
            1,
            64,
            kernel_size=7,
            stride=2,
            padding=3,
            bias=False
        )

        # Freeze ResNet
        for param in self.model.parameters():
            param.requires_grad = False

        # New trainable classifier
        self.model.fc = nn.Linear(
            self.model.fc.in_features,
            num_classes
        )

    def forward(self, x):

        return self.model(x)