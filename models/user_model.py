# models/user_model.py
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional, List, Dict

import re


# 사용자 정보 in-memory 저장소
users: List[Dict] = [
    {"email" : "test@startupcode.kr", "password" : "Test1234!", "nickname" : "startup", "profile_image" : "https://image.kr/img.jpg"}
]


""" ----------------------------- 로그인 관련 ----------------------------- """

# 로그인 요청 DTO
class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="")
    password: str = Field(..., description="")

    # 비밀번호 유효성 검사
    @field_validator("password")
    @classmethod
    def password_rule(cls, value: str) -> str:
        if not value or value.strip() == "":
            raise ValueError("password_required")

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,20}$'
        if not re.match(pattern, value):
            raise ValueError("invalid_password_rule")
        
        return value

# 로그인 응답 DTO
class LoginResponse(BaseModel):
    message: str
    data: Optional[dict] = None