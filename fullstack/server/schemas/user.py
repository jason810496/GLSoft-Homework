from typing import Optional , List 
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    username: str
    birthday: str

class UserCreate(UserBase):
    password: str
    create_time: datetime
    

class UserData(UserBase):
    last_login: Optional[datetime] = None

    class Config:
        orm_mode = True