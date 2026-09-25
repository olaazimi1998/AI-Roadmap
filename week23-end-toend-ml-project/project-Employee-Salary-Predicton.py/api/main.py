from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Employee salary Prediction API"
)

model = joblib.load(
    "models/salary_model.pkl"
)

@app.get("/")
def home():
    return{

        "messege": "Employee Salary prediction API"
    }
@app.post("/predict")
def predict(
    age: int,
    experience: int,
    education: str

):

    data = pd.DataFrame([
        {
            "age": age,
            "experience": experience,
            "education": education
        
        }
    ])

    prediction = model.predict(data)

    return {
        "predicted_salary": float(prediction[0])
    }
#uvicorn api.main:app --reload