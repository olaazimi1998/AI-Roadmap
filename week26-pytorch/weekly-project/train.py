import torch
import torch.nn as nn
from pathlib import Path

from model import MyModel

x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y = torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0]
])

model = MyModel()

loss_function = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)


for epoch in range(1000):

    prediction = model(x)

    loss = loss_function(prediction, y)

    loss.backward()

    optimizer.step()

    optimizer.zero_grad()

    if epoch % 100 == 0:
        print(
            f"Epoch: {epoch}, Loss: {loss.item():.4f}"
        )


test = torch.tensor([[6.0]])

result = model(test)

print("Prediction for 6:", result.item())


model_path = Path(__file__).with_name("model.pth")
torch.save(model.state_dict(), model_path)

print(f"Model saved to {model_path}")