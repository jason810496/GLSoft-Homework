from fastapi import APIRouter, HTTPException, Depends , status
from auth.auth import oauth2_scheme, create_access_token, validate_user, get_current_user
from schemas.token import Token
from schemas.user import UserData , UserCreate , UserQuery , UserInDB
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
        data={"username": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/logout")
async def logout():
    pass

@router.post("/user")
async def register(new_user: UserCreate , db:Session = Depends(get_db)):
    print( "new user>>> :" , new_user , type(new_user) ) 
    db_user = crud_user.get_user_by_username(db,new_user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    crud_user.create_user(db,new_user)
    return status.HTTP_201_CREATED

@router.get("/user" , response_model=List[UserData])
async def get_user( db:Session = Depends(get_db) ):
    return crud_user.get_user_list(db)
    

@router.get("/user/{username}" )
async def get_user_by_username(username : str , db:Session = Depends(get_db)):
    db_user = crud_user.get_user_by_username(db,username=username)
    print( "db_user >>> " , db_user )
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/user/{username}")
async def delete_user( user : UserQuery, db:Session = Depends(get_db) ):
    return crud_user.delete_user(db,user.username)

@router.put("/user/{username}" , response_model=UserData )
async def update_user( user : UserCreate, db:Session = Depends(get_db) ):
    db_user = crud_user.get_user_by_username(db,user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud_user.update_user(db,user)

@router.put("/user/{username}/password")
async def update_password( user : UserCreate , db:Session = Depends(get_db) ):
    return crud_user.update_password(db,user)

@router.put("/user/{username}/birthday")
async def update_birthday( user : UserCreate , db:Session = Depends(get_db) ):
    return crud_user.update_password(db,user)

@router.get("/protected")
async def protected( current_user : UserData = Depends(get_current_user) ):
    return {"message": "Hello World" , "user": current_user }

# debug only
@router.get("/whoami")
async def read_users_me( current_user : UserData = Depends(get_current_user) ):
    return current_user