from fastapi import APIRouter, HTTPException, Depends
from service.auth_service import register_user, authenticate_user
from security import get_current_user
from pydantic import BaseModel

router = APIRouter()

class UserRegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool

class LoginRequest(BaseModel):
    username: str
    password: str

# Initial registration API of a user/admin
@router.post("/register")
def register(data: UserRegisterRequest):
    register_user(data.dict())
    return {"msg": "User/Admin registered successfully"}

# Login API which provides the unique authorization bearer token
@router.post("/login")
def login(data: LoginRequest):
    token = authenticate_user(data.username, data.password)
    if token:
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")

# @router.get("/me")
# def read_users_me(current_user: dict = Depends(get_current_user)):
#     return current_user