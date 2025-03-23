#JWT токен авторизация на сервере

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm


from db.repository import UserRepository
from services import AuthService

from db import *

router = APIRouter()

sqliteRepository = UserRepository()


# jwt auth
@router.post("/auth/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = AuthService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    sqliteRepository.update_user_state(user, "active")  

    return {"access_token": AuthService.create_access_token(data={"sub": user.email})}



@router.post("/auth/register")
async def register(form_data: OAuth2PasswordRequestForm = Depends()):
    user = AuthService.register_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    

    
    sqliteRepository.create_user(user)  

    return {"access_token": AuthService.create_access_token(data={"sub": user.email})}

# logout route to deactivate user

@router.post("/auth/logout")
async def logout(user):
    sqliteRepository.update_user_state(user, "inactive")  
    return {"message": "Logged out successfully"}
 