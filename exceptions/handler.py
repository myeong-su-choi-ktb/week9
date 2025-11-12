# exceptions/handlers.py
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from utils.formatter import create_json_response


# ValueError
VALUE_ERROR_MAP = {
    "invalid_credentials": (status.HTTP_401_UNAUTHORIZED, "*아이디 또는 비밀번호를 확인해주세요."),
    "email_exists": (status.HTTP_409_CONFLICT, "*중복된 이메일입니다."),
    "nickname_exists": (status.HTTP_409_CONFLICT, "*중복된 닉네임입니다."),
    "user_not_found": (status.HTTP_404_NOT_FOUND, "*존재하지 않는 사용자입니다."),
    "post_not_found": (status.HTTP_404_NOT_FOUND, "*존재하지 않는 게시글입니다."),
}

# RequestValidationError
VALIDATION_ERROR_MAP = {
    "value is not a valid email address": "*올바른 이메일 주소 형식을 입력해주세요.",
    "email_required": "*이메일을 입력해주세요.",

    "password_required": "*비밀번호를 입력해주세요.",
    "invalid_password_rule": "비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 합니다.",
    "password_confirm_required": "*비밀번호를 한번 더 입력해주세요.",
    "password_not_match": "*비밀번호가 다릅니다.",

    "profile_image_required": "*프로필 사진을 추가해주세요.",

    "nickname_required": "*닉네임을 입력해주세요.",
    "nickname_no_space": "*띄어쓰기를 없애주세요.",
    "nickname_max_length": "*닉네임은 최대 10자까지 작성 가능합니다.",

    "user_not_found": "*존재하지 않는 사용자입니다.",

    "title_and_content_required": "*제목, 내용을 모두 작성해주세요.",
    "title_too_long": "*제목은 26자 이내로 작성해주세요."
}


# ValueError 처리
async def value_error_exception_handler(request: Request, exc: ValueError):
    msg = str(exc)
    print("🔥 ValueError:", msg)

    for key, (status_code, message) in VALUE_ERROR_MAP.items():
        if key in msg:  # ✅ 부분 문자열 매칭 (contains)
            return create_json_response(status_code, message)
        
    return create_json_response(status.HTTP_400_BAD_REQUEST, "invalid_request")


# 요청 데이터 유효성 검증 실패 처리
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    for error in exc.errors():
        msg = error.get("msg")
        print("🔥 Validation Error:", msg)

        for key, message in VALIDATION_ERROR_MAP.items():
            if key in msg:
                return create_json_response(status.HTTP_422_UNPROCESSABLE_ENTITY, message)
        
        return create_json_response(status.HTTP_422_UNPROCESSABLE_ENTITY, "invalid_request")


# 예상치 못한 서버 내부 오류 처리
async def server_exception_handler(request: Request, exc: Exception):
    return create_json_response(status.HTTP_500_INTERNAL_SERVER_ERROR, "internal_server_error")

