from typing import Optional
from pydantic import BaseModel
from datetime import datetime , date

class UserBase(BaseModel):
    username: str
    birthday: date

class UserCreate(UserBase):
    password: str
    create_time: Optional[datetime] = None
    
class UserData(UserBase):
    last_login: Optional[datetime] = None

class UserPassword(BaseModel):
    password: str

class UserBirthday(BaseModel):
    birthday: date