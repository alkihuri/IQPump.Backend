 # CRUD операции

from sqlalchemy.orm import Session

from models.user import User
 

class userepository:   

    users = []

    def __init__(self) -> None:
        self.users = []

    def create_user(user: User):  
        userepository.users.append(user)
        print(userepository.users)  
        return user


    def update_user_state( user: User, state: bool): 
        user.state = state
        print(user, state)
        return user
