# routers/user_router.py
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from models.user_model import UserLogin, UserSignup, UserEdit, UserPasswordEdit
from controllers.user_controller import login_service, signup_service, edit_user_service, delete_user_service, edit_password_service 
from utils.formatter import create_json_response


router = APIRouter(prefix="/users")

# 사용자 로그인 API
@router.post("/login")
async def login(login_dto: UserLogin) -> JSONResponse:
    data = await login_service(login_dto)
    return create_json_response(status_code=status.HTTP_200_OK, message="로그인 성공", data=data)


# 사용자 회원가입 API
@router.post("/signup")
async def singup(signup_dto: UserSignup) -> JSONResponse:
    data = await signup_service(signup_dto)
    return create_json_response(status_code=status.HTTP_201_CREATED, message="회원가입 성공", data=data)


# 회원 정보 수정 API
@router.patch("/{user_id}/profile")
async def edit_user(user_id: int, user_edit_dto: UserEdit) -> JSONResponse:
    data = await edit_user_service(user_id, user_edit_dto)
    return create_json_response(status_code=status.HTTP_200_OK, message="회원 정보 수정 성공", data=data)


# 회원 탈퇴 API
@router.delete("/{user_id}")
async def delete_user(user_id: int) -> JSONResponse:
    data = await delete_user_service(user_id)
    return create_json_response(status_code=status.HTTP_200_OK, message="회원 탈퇴 성공", data=data)


# 비밀번호 수정 API
@router.patch("/{user_id}/password")
async def edit_password(user_id: int, dto: UserPasswordEdit) -> JSONResponse:
    data = await edit_password_service(user_id, dto)
    return create_json_response(status_code=status.HTTP_200_OK, message="비밀번호 수정 성공", data=data)