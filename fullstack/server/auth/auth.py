from passlib.context import CryptContext
from models.database import get_db ,SessionLocal
from schemas.token import Token
from crud.user import get_user_by_username
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
# for JWT
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional , Annotated
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def validate_user(username: str, password: str):
    user = get_user_by_username(username=username)
    if not user:
        return False

    if not verify_password(password, user.password):
        return False
    return user

async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES",30))
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.environ.get("SECRET_KEY"), algorithm=os.environ.get("JWT_ALGORITHM","HS256"))
    return encoded_jwt


async def get_current_user(token: Annotated[ str , Depends(oauth2_scheme) ]):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, os.environ.get("SECRET_KEY"), algorithms=[os.environ.get("JWT_ALGORITHM","HS256")])
        username: str = payload.get("username")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(username=username)
    if user is None:
        raise credentials_exception
    return user


