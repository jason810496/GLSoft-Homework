from fastapi import APIRouter, HTTPException, Depends , status
from auth.auth import oauth2_scheme, create_access_token, validate_user, get_current_user
from schemas.token import Token
from schemas.user import UserData , UserCreate
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional , Annotated , List
from datetime import datetime, timedelta
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
        data={"usr": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/logout")
async def logout():
    pass

@router.post("/user" , response_model=UserData)
async def register(new_user: UserCreate , db:Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db,new_user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud_user.create_user(db,new_user)

@router.get("/user" , response_model=List[UserData])
async def get_user( db:Session = Depends(get_db) ):
    return crud_user.get_user_list(db)
    

@router.get("/user/{username}" , response_model=UserData )
async def get_user_by_username():
    pass

@router.put("/user")
async def update_user():
    pass

@router.delete("/user/{username}")
async def delete_user():
    pass

@router.put("/user/{username}/password")
async def update_password():
    pass

@router.put("/user/{username}/birthday")
async def update_birthday():
    pass

# debug only
@router.get("/users/me/", response_model=Token)
async def read_users_me( current_user: UserData = Depends(get_current_user) ):
    return {"usr" : current_user}