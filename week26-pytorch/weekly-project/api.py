from fastapi import FastAPI
from pathlib import Path
import torch
import uvicorn

from model import MyModel


app = FastAPI()

MODEL_PATH = Path(__file__).with_name("model.pth")


# Load model
model = MyModel()

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model checkpoint not found at {MODEL_PATH}. Run 'python train.py' first."
    )

model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))

model.eval()


@app.get("/")
def home():
    return {
        "message": "PyTorch Model API is running"
    }


@app.get("/predict")
def predict(x: float):

    input_data = torch.tensor([[x]])

    with torch.no_grad():
        prediction = model(input_data)

    return {
        "input": x,
        "prediction": prediction.item()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)