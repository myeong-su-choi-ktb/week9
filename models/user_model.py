# models/user_model.py
from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict
from validators.user_validator import validate_email, validate_password, validate_password_confirm, validate_profile_iamge, validate_nickname


# 사용자 정보를 임시로 저장하는 in-memory 저장소
users: List[Dict] = [
    {"id": 1, "email" : "test1@test.com", "password" : "Test1234!", "nickname" : "abcd", "profile_image" : "https://image.kr/img1.jpg"},
    {"id": 2, "email" : "test2@test.com", "password" : "Test1234!", "nickname" : "efgh", "profile_image" : "https://image.kr/img2.jpg"},
    {"id": 3, "email" : "test3@test.com", "password" : "Test1234!", "nickname" : "ijkl", "profile_image" : "https://image.kr/img3.jpg"},
    {"id": 4, "email" : "test4@test.com", "password" : "Test1234!", "nickname" : "mnop", "profile_image" : "https://image.kr/img4.jpg"},
    {"id": 5, "email" : "test5@test.com", "password" : "Test1234!", "nickname" : "qrst", "profile_image" : "https://image.kr/img5.jpg"}
]


""" ----------------------------- 로그인 관련 ----------------------------- """

# 로그인 요청 DTO
class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="") # 이메일 형식 검사
    password: str = Field(..., description="")
    
    # 이메일 입력 여부 확인
    @field_validator("email", mode="before")
    @classmethod
    def email_check(cls, value):
        return validate_email(value)
    
    # 비밀번호 유효성 검사
    @field_validator("password")
    @classmethod
    def password_check(cls, value):
        return validate_password(value)


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
    def email_check(cls, value):
        return validate_email(value)

    # 비밀번호 유효성 검사
    @field_validator("password")
    @classmethod
    def password_check(cls, value):
        return validate_password(value)
    
    # 비밀번호 확인 검사
    @field_validator("password_confirm")
    @classmethod
    def password_confirm_check(cls, value, info) -> str:
        return validate_password_confirm(value, info.data.get("password"))
    
    # 프로필 이미지 검증
    @field_validator("profile_image")
    @classmethod
    def profile_image_check(cls, value):
        return validate_profile_iamge(value)
    
    # 닉네임 유효성 검사
    @field_validator("nickname")
    @classmethod
    def nickname_check(cls, value):
        return validate_nickname(value)


""" ----------------------------- 회원 정보 수정 관련 ----------------------------- """

# 회원정보 수정 요청 DTO
class UserEdit(BaseModel):
    nickname: str = Field(..., description="")
    profile_image: str = Field(..., description="")

    # 닉네임 유효성 검사
    @field_validator("nickname")
    @classmethod
    def nickname_check(cls, value):
        return validate_nickname(value)


""" ----------------------------- 비밀번호 수정 관련 ----------------------------- """

# 비밀번호 수정 DTO
class UserPasswordEdit(BaseModel):
    password: str = Field(..., description="")
    password_confirm: str = Field(..., description="")

    # 비밀번호 유효성 검사
    @field_validator("password")
    @classmethod
    def password_check(cls, value):
        return validate_password(value)
    
    # 비밀번호 확인 검사
    @field_validator("password_confirm")
    @classmethod
    def password_confirm_check(cls, value, info) -> str:
        return validate_password_confirm(value, info.data.get("password"))