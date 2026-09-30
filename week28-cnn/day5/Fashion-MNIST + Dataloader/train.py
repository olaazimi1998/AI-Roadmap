import torch
import torch.nn as nn
import torch.optim as optim
from pathlib import Path

from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader

from models.cnn import SimpleCNN

PROJECT_DIR = Path(__file__).resolve().parent


# Dataset
transform = transforms.ToTensor()

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


# DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)


# Model
model = SimpleCNN()


# Loss
criterion = nn.CrossEntropyLoss()


# Optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# Training
num_epochs = 5

for epoch in range(num_epochs):

    model.train()

    running_loss = 0.0

    for images, labels in train_loader:

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

    average_loss = running_loss / len(train_loader)

    print(
        f"Epoch [{epoch + 1}/{num_epochs}], "
        f"Loss: {average_loss:.4f}"
    )


# Save
torch.save(
    model.state_dict(),
    PROJECT_DIR / "models" / "cnn_fashionmnist.pth"
)

print("Model saved!")