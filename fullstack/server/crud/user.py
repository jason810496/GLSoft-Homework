from sqlalchemy.orm import Session
from datetime import datetime

from models.database import SessionLocal
from models.user import UserModels
from schemas.user import UserCreate , UserData

def get_user_by_username(username: str):
    db = SessionLocal()
    return db.query(UserModels).filter(UserModels.username == username).first()

def get_users(db: Session):
    return db.query(UserModels).all()

def create_user(db:Session,user: UserCreate):
    print("birthday: ", datetime.strptime(user.birthday, '%Y-%m-%d').date() )
    db_user = UserModels(username=user.username, password=user.password, birthday=datetime.strptime(user.birthday, '%Y-%m-%d') )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user: UserData):
    db_user = db.query(UserModels).filter(UserModels.username == user.username).first()
    db_user.username = user.username
    db_user.birthday = user.birthday
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
    print("db_user_list: ", db_user)
    return db_user