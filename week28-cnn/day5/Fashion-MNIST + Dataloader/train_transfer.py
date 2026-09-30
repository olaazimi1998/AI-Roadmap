import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path

from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader

from models.resnet import ResNetClassifier

PROJECT_DIR = Path(__file__).resolve().parent


transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


train_dataset = datasets.FashionMNIST(
    root=PROJECT_DIR / "data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = datasets.FashionMNIST(
    root=PROJECT_DIR / "data",
    train=False,
    download=True,
    transform=transform
)


train_loader = DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)


model = ResNetClassifier(
    num_classes=10
)


criterion = nn.CrossEntropyLoss()


optimizer = optim.Adam(
    filter(
        lambda p: p.requires_grad,
        model.parameters()
    ),
    lr=0.001
)


num_epochs = 3

for epoch in range(num_epochs):

    model.train()

    running_loss = 0.0

    for images, labels in train_loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(
            outputs,
            labels
        )

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    average_loss = (
        running_loss /
        len(train_loader)
    )

    print(
        f"Epoch [{epoch + 1}/{num_epochs}], "
        f"Loss: {average_loss:.4f}"
    )


torch.save(
    model.state_dict(),
    PROJECT_DIR / "models" / "resnet_fashionmnist.pth"
)

print("ResNet saved!")