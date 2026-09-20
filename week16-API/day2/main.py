# post is normally used for sending and creating new data.
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Student(BaseModel):

    name: str
    score: int


students = []


@app.get("/")
def home():
    return {"message: Students API is running"}

@app.get("/students")
def get_students():
    return students


@app.post("/students")
def create_student(student: Student):
    students.append(student)

    return {
        "message": "Student created successfully",
        "student": student
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


