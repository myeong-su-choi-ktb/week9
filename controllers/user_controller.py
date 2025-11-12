# controllers/user_controller.py
from fastapi import status
from fastapi.responses import JSONResponse
from models.user_model import *


# 사용자 로그인 서비스
def login_user(login_dto: UserLogin) -> LoginResponse:
    for user in users:
        if user["email"] == login_dto.email and user["password"] == login_dto.password:
            return LoginResponse(
                message="로그인 성공",
                data={"email": login_dto.email}
            )
        
    return LoginResponse(message="*아이디 또는 비밀번호를 확인해주세요.", data=None)

# 사용자 회원가입 서비스
def signup_user(signup_dto: UserSignup) -> SignupResponse:

    # 이메일이 중복되는 경우
    if any(user["email"] == signup_dto.email for user in users):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": "*중복된 이메일입니다.",
                "data": None
            }
        )
    
    # 닉네임이 중복되는 경우
    if any(user["nickname"] == signup_dto.nickname for user in users):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": "*중복된 닉네임입니다.",
                "data": None
            }
        )
    
    # 회원 저장
    new_user = {
        "id": len(users) + 1,
        "email": signup_dto.email,
        "password": signup_dto.password,
        "nickname": signup_dto.nickname,
        "profile_image": signup_dto.profile_image
    }
    users.append(new_user)

    return SignupResponse(
        message="회원가입 성공",
        data={
            "user_id": new_user["id"],
            "email": new_user["email"],
            "password": new_user["password"],
            "nickname": new_user["nickname"],
            "profile_image": new_user["profile_image"]
        }
    )

# 회원 정보 수정 서비스
def edit_user(user_id: int, edit_dto: UserEdit) -> SignupResponse:
    
    target = next((user for user in users if user["id"] == user_id), None)
    if not target:
        raise ValueError("user_not_found")

    # 닉네임이 중복되는 경우
    if any(user["nickname"] == edit_dto.nickname for user in users):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": "*중복된 닉네임입니다.",
                "data": None
            }
        )
    
    # 수정 반영
    target["nickname"] = edit_dto.nickname
    target["profile_image"] = edit_dto.profile_image

    return SignupResponse(
        message="회원정보 수정 성공",
        data={
            "id": target["id"],
            "nickname": target["nickname"],
            "profile_image": target["profile_image"]
        }
    )
