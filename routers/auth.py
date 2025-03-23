from fastapi import APIRouter
from models import User
from db import repository
router = APIRouter()


@router.post("/auth/login/")
def login(data : User): 
    repository.userepository.update_user_state(data, True)
    return {"message": "Login route"}  



@router.post("/auth/register/")
def register(data : User):

    repository.userepository.create_user(data)
    return {"message": "Register route"} 
    