from sqlalchemy.orm import Session
from datetime import datetime

from models.database import SessionLocal
from models.user import UserModels
from schemas.user import UserCreate , UserData , UserBase
from typing import List

def get_user_by_username(username: str):
    db = SessionLocal()
    return db.query(UserModels).filter(UserModels.username == username).first()

def get_users():
    db = SessionLocal()
    # db_user_list = db.query(UserModels).all()
    # result = []
    # for db_user in db_user_list:
    #     result.append(UserBase(username=db_user.username , birthday=db_user.birthday))
    # return result
    return db.query(UserModels).all()

def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = UserModels(username=user.username, password=user.password, birthday=user.birthday )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_login(username: str):
    db = SessionLocal()
    db_user = db.query(UserModels).filter(UserModels.username == username).first()
    db_user.last_login = datetime.now()
    db.commit()
    db.refresh(db_user)
    return db_user

def update_birthday(username : str , birthday : datetime):
    db = SessionLocal()
    db_user = db.query(UserModels).filter(UserModels.username == username).first()
    db_user.birthday = birthday
    db.commit()
    db.refresh(db_user)
    return db_user

def update_password(username: str , password: str ):
    db = SessionLocal()
    db_user = db.query(UserModels).filter(UserModels.username == username).first()
    db_user.password = password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(username: str):
    db = SessionLocal()
    db_user = db.query(UserModels).filter(UserModels.username == username).first()
    db.delete(db_user)
    db.commit()
    return db_user

def get_user_list():
    db = SessionLocal()
    db_user = db.query(UserModels).all()
    print("db_user_list: ", db_user)
    return db_user