import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from pathlib import Path

from torch.utils.data import DataLoader
from torchvision.datasets import FashionMNIST

from models.cnn import SimpleCNN

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])

project_dir = Path(__file__).resolve().parent
data_dir = project_dir / "data"

train_dataset = FashionMNIST(
    root=data_dir,
    train=True,
    download=True,
    transform=transform
)

test_dataset = FashionMNIST(
    root=data_dir,
    train=False,
    download=True,
    transform=transform
)

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

model = SimpleCNN()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)

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

    print(
        f"Epoch [{epoch + 1}/{num_epochs}], "
        f"Loss: {running_loss / len(train_loader):.4f}"
    )


torch.save(
    model.state_dict(),
    project_dir / "models" / "cnn.pth"
)
