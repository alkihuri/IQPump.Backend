from fastapi import APIRouter
from models import User
from db import repository
router = APIRouter()


@router.get("/auth/login/")
def login(User):

    if User:
        return {"message": "Login route"} 
    
    repository.userepository.update_user_state(User, "active")



@router.get("/auth/register/")
def register(User):

    if User:
        return {"message": "Register route"} 
    
    repository.userepository.create_user(User)