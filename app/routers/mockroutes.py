


# mock routes for testing purposes only

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/mock/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# register a new user
@router.post("/mock/register")
async def register_user(user: dict):
    return user

# login a user
@router.post("/mock/login")
async def login_user(user: dict):
    return user

# get all users

@router.get("/mock/users")
async def get_users():
    return {"users": "users"}

# get user by id
@router.get("/mock/user/{user_id}") 
async def get_user(user_id: int):
    return {"user_id": user_id}

# update user by id
@router.put("/mock/user/{user_id}")
async def update_user(user_id: int, user: dict):
    return {"user_id": user_id, "user": user}