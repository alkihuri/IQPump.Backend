 # Подбор соперников

from  fastapi import APIRouter
from  models import User
from   db import *
from  db.session import Session

router = APIRouter()
# only with auth
@router.get("/opponents")
def find_opponents():
    with Session(db.engine.url) as cursor:
        cursor.execute("SELECT * FROM users")
        opponents = cursor.fetchall()
    return [User(*opponent) for opponent in opponents]
 

@router.get("/opponents/{user_id}")
def find_opponents(user_id: int):
    with Session(db.engine.url) as cursor:
        cursor.execute("SELECT * FROM users WHERE id == ", (user_id,))
        opponents = cursor.fetchall()
    return  opponents[0]