# controllers/user_controller.py
from models.user_model import users # DB 대체
from models.user_model import UserLogin, UserSignup, UserEdit, UserPasswordEdit


# 사용자 로그인 서비스
async def login_service(login_dto: UserLogin) -> dict:

    # 이메일과 비밀번호가 일치하는 사용자 찾기
    for user in users:
        if user["email"] == login_dto.email and user["password"] == login_dto.password:
            return {
                "email": user["email"],
                "nickname": user["nickname"],
                "profile_image": user["profile_image"]
            }

    # 로그인 실패   
    raise ValueError("invalid_credentials")


# 사용자 회원가입 서비스
async def signup_service(signup_dto: UserSignup) -> dict:

    # 이메일 중복 검사
    if any(user["email"] == signup_dto.email for user in users):
        raise ValueError("email_exists")
    
    # 닉네임 중복 검사
    if any(user["nickname"] == signup_dto.nickname for user in users):
        raise ValueError("nickname_exists")
    
    # ID 자동 증가
    next_id = max([user["id"] for user in users]) + 1 if users else 1
    
    # 신규 회원 저장
    new_user = {
        "id": next_id,
        "email": signup_dto.email,
        "password": signup_dto.password,
        "nickname": signup_dto.nickname,
        "profile_image": signup_dto.profile_image
    }
    users.append(new_user)

    return {
        "user_id": new_user["id"],
        "email": new_user["email"],
        "password": new_user["password"],
        "nickname": new_user["nickname"],
        "profile_image": new_user["profile_image"]
    }


# 회원 정보 수정 서비스
async def edit_user_service(user_id: int, user_edit_dto: UserEdit) -> dict:
    
    # 수정할 사용자 찾기
    target = next((user for user in users if user["id"] == user_id), None)
    if not target:
        raise ValueError("user_not_found")

    # 닉네임 중복 검사
    if any(user["nickname"] == user_edit_dto.nickname and user["id"] != user_id for user in users):
        raise ValueError("nickname_exists")
    
    # 수정 반영
    target["nickname"] = user_edit_dto.nickname
    target["profile_image"] = user_edit_dto.profile_image

    return {
        "id": target["id"],
        "nickname": target["nickname"],
        "profile_image": target["profile_image"]
    }


# 회원 탈퇴 서비스
async def delete_user_service(user_id: int) -> dict:
    # 사용자 존재 여부 확인
    target = next((user for user in users if user["id"] == user_id), None)
    if not target:
        raise ValueError("user_not_found")
    
    deleted_user = {
        "id": target["id"],
        "email": target["email"],
        "nickname": target["nickname"],
        "profile_image": target["profile_image"]
    }

    # 리스트에서 해당 사용자 제거
    users.remove(target)

    return deleted_user


# 비밀번호 수정 서비스
async def edit_password_service(user_id: int, password_dto: UserPasswordEdit) -> dict:

    # 수정할 사용자 찾기
    target = next((user for user in users if user["id"] == user_id), None)
    if not target:
        raise ValueError("user_not_found")
    
    # 비밀번호 변경
    target["password"] = password_dto.password

    return {
        "id": target["id"], 
        "email": target["email"]
    }