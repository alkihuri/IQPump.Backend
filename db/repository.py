 # CRUD операции

from sqlalchemy.orm import Session
from models import User

class UserRepository:   

    def get_user(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()



    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()


    def create_user(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user


    def update_user_state(db: Session, user: User, state: str):
        user.state = state
        db.commit()
        db.refresh(user)
        return user
