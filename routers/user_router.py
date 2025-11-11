# routers/user_router.py
from fastapi import APIRouter, status

from models.user_model import *
from controllers.user_controller import *


router = APIRouter(prefix="/users")

# 사용자 로그인 API
@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginResponse)
def login(login_dto: UserLogin):
    return user_login(login_dto)
