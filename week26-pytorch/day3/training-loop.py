import torch
import torch.nn as nn 


x = torch.tensor([[1.0], [2.0],[3.0],[4.0]])
y = torch.tensor([[2.0],[4.0],[6.0] ,[8.0]])


class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)


    def forward(self, x):
        return self.linear(x)

model = MyModel()


loss_function = nn.MSELoss()

optimizer = torch.optim.SGD(model.parameters(),
                            lr=0.01)

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

test = torch.tensor([[5.0]])

result = model(test)
print("prediction for 5:", result.item())


