# models/user_model.py
from pydantic import BaseModel, EmailStr, ValidationInfo, Field, field_validator
from typing import Optional, List, Dict
import re


# 사용자 정보 in-memory 저장소
users: List[Dict] = [
    {"id": 1, "email" : "test@startupcode.kr", "password" : "Test1234!", "nickname" : "startup", "profile_image" : "https://image.kr/img.jpg"}
]


""" ----------------------------- 로그인 관련 ----------------------------- """

# 로그인 요청 DTO
class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="") # 이메일 형식 검사
    password: str = Field(..., description="")
    
    # 이메일 입력 여부 확인
    @field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, value):
        if not value or value.strip() == "":
            raise ValueError("email_required")
        return value
    
    # 비밀번호 유효성 검사
    @field_validator("password")
    @classmethod
    def password_rule(cls, value):
        # 비밀번호 입력 안했을 시
        if not value or value.strip() == "":
            raise ValueError("password_required")

        # 8자 이상, 20자 이하 / 대문자, 소문자, 숫자, 특수문자 최소 1개 포함
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,20}$'
        if not re.match(pattern, value):
            raise ValueError("invalid_password_rule")
        
        return value

# 로그인 응답 DTO
class LoginResponse(BaseModel):
    message: str
    data: Optional[dict] = None


""" ----------------------------- 회원가입 관련 ----------------------------- """

# 회원가입 요청 DTO
class UserSignup(BaseModel):
    email: EmailStr = Field(..., description="")
    password: str = Field(..., description="")
    password_confirm: str = Field(..., description="")
    nickname: str = Field(..., description="")
    profile_image: str = Field(..., description="")

    # 이메일 입력 여부 확인
    @field_validator("email", mode="before")
    @classmethod
    def validate_email(cls, value):
        if not value or value.strip() == "":
            raise ValueError("email_required")
        return value

    # 비밀번호 유효성 검사
    @field_validator("password")
    @classmethod
    def password_rule(cls, value):
        if not value or value.strip() == "":
            raise ValueError("password_required")

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,20}$'
        if not re.match(pattern, value):
            raise ValueError("invalid_password_rule")
        
        return value
    
    # 비밀번호 확인 검사
    @field_validator("password_confirm")
    @classmethod
    def confirm_password(cls, value, info) -> str:
        # 비밀번호 확인 입력 안했을 시
        if not value or value.strip() == "":
            raise ValueError("password_confirm_required")

        # 비밀번호가 확인과 다를 시
        if "password" in info.data and value != info.data["password"]:
            raise ValueError("password_not_match")
        return value
    
    # 프로필 이미지 검증
    @field_validator("profile_image")
    @classmethod
    def validate_profile_image(cls, value):
        if not value or value.strip() == "":
            raise ValueError("profile_image_required")
        return value
    
    # 닉네임 유효성 검사
    @field_validator("nickname")
    @classmethod
    def validate_nickname(cls, value):
        # 닉네임 입력하지 않을 시
        if not value or value.strip() == "":
            raise ValueError("nickname_required")
        
        # 닉네임 띄어쓰기 불가
        if " " in value:
            raise ValueError("nickname_no_space")
        
        # 닉네임 10글자 이내
        if len(value) > 10:
            raise ValueError("nickname_max_length")
        
        return value
    
# 회원가입 응답 DTO
class SignupResponse(BaseModel):
    message: str
    data: Optional[Dict] = None


""" ----------------------------- 회원 정보 수정 관련 ----------------------------- """

# 회원정보 수정 요청 DTO
class UserEdit(BaseModel):
    nickname: str = Field(..., description="")
    profile_image: str = Field(..., description="")

    # 닉네임 유효성 검사
    @field_validator("nickname")
    @classmethod
    def validate_nickname(cls, value):
        # 닉네임 입력하지 않을 시
        if not value and value.strip() == "":
            raise ValueError("nickname_required")
        
        # 닉에임 띄어쓰기 불가
        if " " in value:
            raise ValueError("nickname_no_space")
        
        # 닉네임 10글자 이내
        if len(value) > 10:
            raise ValueError("nickname_max_length")
        
        return value
        