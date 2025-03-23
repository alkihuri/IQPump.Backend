 # Подбор соперников

from fastapi import APIRouter

from db.session import Session
from models import User

router = APIRouter()
# only with auth
@router.get("/opponents")
def find_opponents():
    return None
 

@router.get("/opponents/{user_id}")
def find_opponents(user_id: int):
    return None