from sqlalchemy import Session
from . import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password, birthday=user.birthday)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_birthday(db: Session, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    db_user.birthday = user.birthday
    db.commit()
    db.refresh(db_user)
    return db_user

def update_password(db: Session, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, username: str):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    db.delete(db_user)
    db.commit()
    return db_user