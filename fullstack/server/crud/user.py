from sqlalchemy.orm import Session
import datetime

from models.database import Base
from models.user import UserModels
from schemas.user import UserCreate , UserData

# from ..models.user import UserModels
# from ..schemas.user import UserCreate , UserData

def get_user_by_username(db:Session,username: str):
    print("username: ",username)
    db_user = UserModels(username=username, password='123', birthday= datetime("2023-04-04"))
    print("db_user: ",db_user)
    return db.query(UserModels).filter(UserModels.username == username).first()

def get_users(db: Session):
    return db.query(UserModels).all()

def create_user(db:Session,user: UserCreate):
    db_user = UserModels(username=user.username, password=user.password, birthday= datetime(user.birthday))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_birthday(db: Session, user: UserData):
    db_user = db.query(UserModels).filter(UserModels.username == user.username).first()
    db_user.birthday = user.birthday
    db.commit()
    db.refresh(db_user)
    return db_user

def update_password(db: Session, user: UserData):
    db_user = db.query(UserModels).filter(UserModels.username == user.username).first()
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, username: str):
    db_user = db.query(UserModels).filter(UserModels.username == username).first()
    db.delete(db_user)
    db.commit()
    return db_user

def get_user_list(db: Session):
    db_user = db.query(UserModels).all()
    return db_user