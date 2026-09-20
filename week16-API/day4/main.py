"""
User
    ↓
Web / Mobile App
    ↓
FastAPI
    ↓
Request Validation
    ↓
Preprocessing
    ↓
ML Model
    ↓
Prediction
    ↓
FastAPI
    ↓
JSON
    ↓
User
"""

from fastapi import FastAPI

from model import predict
from schema import PredictionRequest, PredictionResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI API is running"}


@app.post("/predict", response_model=PredictionResponse)
def make_prediction(data: PredictionRequest):
    result = predict(data.age, data.salary)

    return {
        "prediction": result
    }
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/users/{user_id}")
def get_user(user_id: int):

    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": 1,
        "name": "Ali"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)