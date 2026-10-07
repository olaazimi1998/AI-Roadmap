from fastapi import FastAPI
from pydantic import BaseModel

from app.model import model
app = FastAPI(
    title="A simple ML API running inside Docker", 
    version="1.0.0"
)
class PredictionRequest(BaseModel):
    value: float

@app.get("/")
def home():
    return {
        "message": "ML API is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = model.predict(request.value)
    return {
        "input": request.value,
        "prediction": prediction 
    }
#docker build -t my-app .
#docker run my-app
#docker run -p 8003:8000 my-app
#write in web browser http://localhost:8003/docs to see the API documentation