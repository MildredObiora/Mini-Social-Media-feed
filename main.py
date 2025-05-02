from fastapi import FastAPI, Form
from pydantic import BaseModel, EmailStr
from typing import Annotated

my_app = FastAPI()

# Pydantic model for user creation
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: str

# Dictionary to simulate storing users (in-memory)
new_user_db: dict[str, UserCreate] = {}

@my_app.get("/")
def home():
    return {"message": "Welcome to Mini Social Media API!"}

@my_app.post("/login/")
async def returning_user_login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    return {"message": f"Hi {username}, welcome back!"}

@my_app.post("/users/")
async def register_user(user: UserCreate):
    if user.username in new_user_db:
        return {"error": "Username already exists"}
    
    new_user_db[user.username] = user
    return {"message": "User registered successfully", "user": user}

@my_app.get("/users/")
async def list_users():
    return {"users": list(new_user_db.values())}
