from fastapi import APIRouter, HTTPException, Depends , status
from auth.auth import oauth2_scheme, create_access_token, validate_user, get_current_user
from schemas.token import Token
from schemas.user import UserData , UserCreate , UserPassword , UserBase , UserBirthday
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional , Annotated , List
from datetime import datetime, timedelta , date
import os
from sqlalchemy.orm import Session
from models.database import get_db
import crud.user as crud_user

router = APIRouter()

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends() ] ):
    user = validate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES",30))
    access_token = await create_access_token(
        data={"username": form_data.username}, expires_delta=access_token_expires
    )
    crud_user.update_user_login(form_data.username)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/user")
async def register(new_user: UserCreate ):
    db_user = crud_user.get_user_by_username(new_user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    crud_user.create_user(new_user)
    return status.HTTP_201_CREATED

@router.get("/user")
async def get_users():
    return crud_user.get_users()
    

@router.get("/user/{username}" , response_model=UserBase)
async def get_user_by_username(username : str ):
    db_user = crud_user.get_user_by_username(username=username)

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserBase(username=db_user.username , birthday=db_user.birthday)

@router.delete("/user")
async def delete_user( current_user : UserData = Depends(get_current_user) ):
    return crud_user.delete_user(current_user.username)

# @router.put("/user/" , response_model=UserData )
# async def update_user( user : UserCreate ):
#     db_user = crud_user.get_user_by_username(user)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return crud_user.update_user(user)

@router.put("/user/password" )
async def update_password( request : UserPassword , current_user : UserData = Depends(get_current_user) ):
    return crud_user.update_password( current_user.username , password=request.password )

@router.put("/user/birthday" )
async def update_birthday( request : UserBirthday  , current_user : UserData = Depends(get_current_user)):
    return crud_user.update_birthday( username=current_user.username ,birthday=request.birthday )

@router.get("/protected")
async def protected( current_user : UserData = Depends(get_current_user) ):
    return {"message": "protected area" , "user": current_user }

# debug only
@router.get("/whoami")
async def read_users_me( current_user : UserData = Depends(get_current_user) ):
    return current_user