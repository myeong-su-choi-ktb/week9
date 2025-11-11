# controllers/user_controller.py
from models.user_model import *


# 사용자 로그인 서비스
def user_login(login_dto: UserLogin) -> LoginResponse:
    for user in users:
        if user["email"] == login_dto.email and user["password"] == login_dto.password:
            return LoginResponse(
                message="로그인 성공",
                data={"email": login_dto.email}
            )
        
    return LoginResponse(message="*아이디 또는 비밀번호를 확인해주세요.", data=None)

