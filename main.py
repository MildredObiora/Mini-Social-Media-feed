from fastapi import FastAPI, Form, HTTPException, status
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

# To unlike a post
@my_app.post("/posts/{post_id}/unlike/")
def unlike_post(post_id: int, username:str):
    for post in posts:
        if post["id"] == post_id:
            if (username, post_id) not in likes:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail = "You have not liked this post yet"
                )
            likes.remove((username, post_id))
            post["likes"] = max(0, post["likes"] - 1)
            return {"Message": "Post unliked!", "likes": post["likes"]}
    raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail = "Post not found"
                )
