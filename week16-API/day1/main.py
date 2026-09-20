from fastapi import FastAPI

app = FastAPI()

students = [
    {"name": "Ali", "score": 85},
    {"name": "Sara", "score": 92},
    {"name": "John", "score": 78},
    {"name": "Mary", "score": 95},
]


@app.get("/students")
def get_students(min_score: int = 0):
    return [student for student in students if student["score"] >= min_score]

@app.get("/")
def home():
	return {"message": "Student API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
