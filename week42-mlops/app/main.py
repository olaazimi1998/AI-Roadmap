from fastapi import FastAPI
from app.schemas import CustomerData

app = FastAPI(
        title="Customer Churn Prediction API",
        description="An ML API built during Week 42",
        version="1.0.0",
    )
@app.get("/")
def home():
    return {
        "message": "customer churn prediction api is running.",
        "status": "healthy",
    }

@app.get("/health")
def health_check():
    return {
         "status": "healthy",
    }


@app.post("/predict")
def predict_churn(customer: CustomerData):
    # Temporary placeholder prediction.
    # We will replace this with a trained model later.
    return {
        "prediction": "unknown",
        "message": "The API works, but the trained ML model is not connected yet.",
        "customer": customer.model_dump(),
    }