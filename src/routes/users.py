from fastapi import APIRouter, HTTPException, status
from src.models.users import User, UserSignIN
from src.database.connection import Database


user_router = APIRouter(
    prefix = "/users",
    tags = ["Users"]
)
user_db = Database(User)

@user_router.post("/signup")
async def sign_net_new_user(user: User):
    user_exist = await user_db.model.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with email provided exists already"
        )
    await user_db.save(user)
    return {
        "message": "User created successfully"
        }

@user_router.post("/signup")
async def sign_new_user(user: User):
    """회원가입"""  
    if user.email in users:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="User already exists"
            )
    users[user.email] = users
    return {"message": "User successfully created", "user": user}

@user_router.post("/signin")
async def sign_user_in(credentials: UserSignIN):
    """회원가입이 끝난 회원 로그인하는 API
    이메일, 비밀번호
    로그인: 이메일, 비밀번호
    """

    if credentials.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User not found"
        )
    stroed_user = users[credentials.email]
    if stroed_user.password != credentials.password:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            deatil = "Invalid password"
        )
    return {"message": "User successfully signed in"}
    
