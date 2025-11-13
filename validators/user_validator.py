import re


# 이메일 입력 여부 확인
def validate_email(value: str) -> str:
    if not value or value.strip() == "":
        raise ValueError("email_required")
    return value

# 비밀번호 유효성 검사
def validate_password(value: str) -> str:
    # 비밀번호 입력 안했을 시
    if not value or value.strip() == "":
        raise ValueError("password_required")

    # 8자 이상, 20자 이하 / 대문자, 소문자, 숫자, 특수문자 최소 1개 포함
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,20}$'
    if not re.match(pattern, value):
        raise ValueError("invalid_password_rule")
    
    return value
    
# 비밀번호 확인 검사
def validate_password_confirm(value: str, password: str) -> str:
    # 비밀번호 확인 입력 안했을 시
    if not value or value.strip() == "":
        raise ValueError("password_confirm_required")

    # 비밀번호가 확인과 다를 시
    if value != password:
        raise ValueError("password_not_match")
    return value

# 프로필 이미지 검증
def validate_profile_iamge(value: str) -> str:
    if not value or value.strip() == "":
        raise ValueError("profile_image_required")
    return value

# 닉네임 검증
def validate_nickname(value: str) -> str:
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