import os
import sys

import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from models.resnet import ResNetClassifier


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])

    train_dataset = datasets.FashionMNIST(
        root=os.path.join(PROJECT_ROOT, "data"),
        train=True,
        download=True,
        transform=transform,
    )
    test_dataset = datasets.FashionMNIST(
        root=os.path.join(PROJECT_ROOT, "data"),
        train=False,
        download=True,
        transform=transform,
    )

    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)

    model = ResNetClassifier(num_classes=10).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.model.fc.parameters(), lr=1e-3)

    model.train()
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        print(f"loss={loss.item():.4f}")
        break

    model.eval()
    with torch.no_grad():
        x, y = next(iter(test_loader))
        x, y = x.to(device), y.to(device)
        logits = model(x)
        preds = logits.argmax(dim=1)
        accuracy = (preds == y).float().mean().item()
        print(f"test_accuracy={accuracy:.4f}")


if __name__ == "__main__":
    main()
