from fastapi import FastAPI, HTTPException
from models.users import User
from fastapi.middleware.cors import CORSMiddleware

origins=[
    "http://localhost:5173",

]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)
user_db = [
    {
        "id": 0,
        "name": "John Doe",
        "age": 25
    },
    {
        "id": 1,
        "name": "Jane Doe",
        "age": 24
    },
    {
        "id": 2,
        "name": "Alice",
        "age": 27
    }
]

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/api/v1/users", response_model=list[User]) 
def get_users():
    return user_db


@app.get("/api/v1/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in user_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/v1/users", response_model=User)
def create_user(user: User):
    for u in user_db:
        if u["id"] == user.id:
            raise HTTPException(status_code=400, detail="User already exists")
    new_user = user.model_dump()
    user_db.append(new_user)
    return new_user

@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id: int):
    for user in user_db:
        if user["id"] == user_id:
            user_db.remove(user)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")