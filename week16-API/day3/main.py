#| Code | Meaning      |
#| ---- | ------------ |
#| 200  | OK           |
#| 201  | Created      |
#| 400  | Bad Request  |
#| 401  | Unauthorized |
#| 403  | Forbidden    |
#| 404  | Not Found    |
#| 500  | Server Error |

#| Method | Purpose             |
#| ------ | ------------------- |
#| GET    | Get data            |
#| POST   | Create/send data    |
#| PUT    | Replace/update data |
#| DELETE | Delete data         |

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int


@app.get("/")
def home():
    return {"message": "hello world"}


@app.get("/about")
def about():
    return {"message": "About page"}


@app.get("/users")
def get_users(age: int | None = None):
    return {"age": age, "users": ["Ali", "Sara", "John"]}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}


@app.post("/users", response_model=User)
def create_user(user: User):
    return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
