from fastapi import FastAPI, Form
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