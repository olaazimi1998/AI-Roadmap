import torch
from pathlib import Path

from torchvision import datasets
from torchvision import transforms
from torch.utils.data import DataLoader

from models.cnn import SimpleCNN

PROJECT_DIR = Path(__file__).resolve().parent


# Dataset
transform = transforms.ToTensor()

test_dataset = datasets.FashionMNIST(
    root=PROJECT_DIR / "data",
    train=False,
    download=True,
    transform=transform
)

test_loader = DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)


# Model
model = SimpleCNN()

model.load_state_dict(
    torch.load(
        PROJECT_DIR / "models" / "cnn_fashionmnist.pth",
        weights_only=True
    )
)

model.eval()


# Evaluation
correct = 0
total = 0

with torch.no_grad():

    for images, labels in test_loader:

        outputs = model(images)

        _, predicted = torch.max(
            outputs,
            1
        )

        total += labels.size(0)

        correct += (
            predicted == labels
        ).sum().item()


accuracy = 100 * correct / total

print(f"Accuracy: {accuracy:.2f}%")