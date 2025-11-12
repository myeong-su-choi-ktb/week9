# routers/user_router.py
from fastapi import APIRouter, status

from models.user_model import *
from controllers.user_controller import *


router = APIRouter(prefix="/users")

# 사용자 로그인 API
@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
def login(login_dto: UserLogin):
    return login_user(login_dto)

# 사용자 회원가입 API
@router.post("/signup", status_code=status.HTTP_201_CREATED)
def singup(signup_dto: UserSignup):
    return signup_user(signup_dto)

# 회원 정보 수정 API
@router.patch("/{user_id}/profile", status_code=status.HTTP_200_OK, response_model=SignupResponse)
def edit_user(user_id: int, user_edit_dto: UserEdit):
    return edit_profile(user_id, user_edit_dto)

# 비밀번호 수정 API
@router.patch("/{user_id}/password", status_code=status.HTTP_200_OK, response_model=SignupResponse)
def edit_user(user_id: int, dto: UserPasswordEdit):
    return edit_password(user_id, dto)