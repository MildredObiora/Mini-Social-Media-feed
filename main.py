from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Annotated, Optional

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

@my_app.post("/users/")
async def register_user(user: UserCreate):
    if user.username in new_user_db:
        return {"error": "Username already exists"}
    
    new_user_db[user.username] = user
    return {"message": "User registered successfully", "user": user}

@my_app.get("/users/")
async def list_users():
    return {"users": list(new_user_db.values())} 

@my_app.post("/login/")
async def returning_user_login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
):
    return {"message": f"Hi {username}, welcome back!"}

posts = {}


class CreatePost(BaseModel):
    id: int
    username: str
    title: str
    content: str
    image_filename: Optional[str] = None
    likes: int = 0

@my_app.get("/user{username}/posts")
async def get_user_post(username: str):
    if username not in new_user_db:
        raise HTTPException(status_code=404, detail="Username not found")
    return [post for post in posts if post.username == username]