from fastapi import APIRouter, HTTPException, Depends

router = APIRouter()

@router.post("/login")
async def login():
    pass

@router.get("/logout")
async def logout():
    pass

@router.post("/user")
async def register():
    pass

@router.get("/user")
async def get_user():
    pass

@router.get("/user/{username}")
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