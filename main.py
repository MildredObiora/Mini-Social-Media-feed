from fastapi import FastAPI, Form, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Annotated, Optional
from fastapi import FastAPI , File ,UploadFile ,Form


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

post_db=[{}]

@my_app.post("/post/")
async def submit_post(
   
    username: str = Form(),
    title: str = Form(),
    content: str = Form(),
    upload_image: Optional[UploadFile] = File(None)
):
    post_id=len(post_db) + 1

@my_app.get("/post/")
async def list_all_posts():
    return {"posts": [post.dict() for post in post_db]}
    
    post_data = CreatePost(
        id=post_id,
        username=username,
        title=title,
        content=content,
    )
    post_db.append(post_data)
    return {"message": "Post submitted successfully", "post": post_data.dict()}
